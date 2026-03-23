/**
 * Chat-to-Jira Integration - Apps Script
 * 
 * Runs when the "Requests" sheet changes. Reads new rows, deduplicates by Message ID,
 * and POSTs to your Jira Automation webhook. Uses LockService to avoid race conditions.
 * 
 * SETUP:
 * 1. In Apps Script: Project Settings (gear) > Script Properties
 *    Add: JIRA_URL = (your Jira webhook URL)
 *    Add: JIRA_SECRET_KEY = (your webhook secret / X-Automation-Webhook-Token value)
 * 2. Add a trigger: From spreadsheet > On change (and choose the function below that processes rows)
 * 
 * SHEET: Tab name must be "Requests". Row 1 headers: Summary | Description | AssigneeEmail | Status | Message ID
 */

const SHEET_NAME = 'Requests';
const LOCK_TIMEOUT_MS = 30000;
const COL_SUMMARY = 1;      // A
const COL_DESCRIPTION = 2;  // B
const COL_ASSIGNEE = 3;     // C
const COL_STATUS = 4;       // D
const COL_MESSAGE_ID = 5;   // E
const JIRA_SUMMARY_MAX_LENGTH = 255;

/**
 * Makes summary precise and crisp: plain text only, no markdown. Prefers question if present, else first short phrase.
 */
function crispSummary(text) {
  if (!text || !text.toString) return '';
  var s = text.toString().trim();
  if (!s) return '';
  s = s.replace(/\r?\n|\r/g, ' ').replace(/\s+/g, ' ').trim();
  // Strip all markdown: **bold** and *italic*
  s = s.replace(/\*\*/g, '').replace(/\*([^*]*)\*/g, '$1');
  // Strip common AI openers (Here is..., Here's..., Certainly!, etc.)
  s = s.replace(/^(Here\'?s? (is|are) (the|a )?|Absolutely!?|Certainly!?|Sure!?|Of course!?|Sure thing!?|No problem!?)\s*/gi, '');
  s = s.replace(/^[::\s\-–—]+\s*/g, '');
  s = s.replace(/\s*#{1,6}\s*/g, ' ');
  // Strip trailing fluff (e.g. "If you need more details... let me know!")
  s = s.replace(/\s*If you need (more )?details[^.!?]*[.!?]\s*$/gi, '');
  s = s.replace(/\s*let me know!?\s*$/gi, '');
  s = s.replace(/\s+$/g, '').trim();
  // Prefer a question (sentence ending with ?) as the summary
  var qMatch = s.match(/[^.?!]*\?/);
  if (qMatch) {
    s = qMatch[0].trim();
  } else {
    var first = s.match(/^[^.!?]+[.!?]?/);
    s = first ? first[0].trim() : s;
  }
  if (s.length > JIRA_SUMMARY_MAX_LENGTH) {
    s = s.substring(0, JIRA_SUMMARY_MAX_LENGTH - 3) + '...';
  }
  return s || '(No summary)';
}

/**
 * Cleans description: strip all ** and * (plain text), format as neat Jira bullets.
 */
function sanitizeForJira(text) {
  if (!text || !text.toString) return '';
  var s = text.toString().trim();
  if (!s) return '';
  // Strip trailing fluff sentence
  s = s.replace(/\n\s*If you need (more )?details[^\n]*$/gi, '');
  s = s.replace(/\n\s*let me know!?\s*$/gi, '');
  var lines = s.split(/\r?\n/);
  var out = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i].trim();
    line = line.replace(/\|/g, ' ');
    // Remove ALL ** (bold) and * used for italic so no raw special chars
    line = line.replace(/\*\*/g, '');
    line = line.replace(/\*([^*]*)\*/g, '$1');
    line = line.replace(/\s+/g, ' ').trim();
    if (/^[\s\-_=]+$/.test(line)) continue;
    line = line.replace(/^#{1,6}\s*/, '');
    line = line.replace(/[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '');
    if (!line) {
      if (out.length > 0 && out[out.length - 1] !== '') out.push('');
      continue;
    }
    // Bullet: line starting with "- " or "* " or "• " -> Jira bullet "* "
    if (/^[\-\*•]\s+/.test(line)) {
      line = '* ' + line.replace(/^[\-\*•]\s+/, '').trim();
    }
    out.push(line);
  }
  return out.join('\n').replace(/\n{3,}/g, '\n\n').trim();
}

/**
 * Call this from an "On change" trigger so the script runs when the sheet is edited.
 * (In trigger setup: From spreadsheet > On change > processSheetOnChange)
 */
function processSheetOnChange(e) {
  var ss = (e && e.source) ? e.source : SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) return;
  processPendingRows(sheet);
}

/**
 * Alternative: run manually or from a trigger that fires on edit.
 * Processes any row that has a Message ID but Status is empty or "PENDING".
 */
function processPendingRows(sheet) {
  if (!sheet) sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
  if (!sheet) {
    Logger.log('Sheet "' + SHEET_NAME + '" not found.');
    return;
  }

  var lock = LockService.getScriptLock();
  if (!lock.tryLock(LOCK_TIMEOUT_MS)) {
    // Time out silently to avoid duplication; next trigger will retry.
    return;
  }
  try {
    var data = sheet.getDataRange().getValues();
    if (data.length < 2) return; // Header only

    var header = data[0];
    var lastRow = data.length;
    var updates = []; // [ [rowIndex, statusValue], ... ]

    for (var i = 1; i < data.length; i++) {
      var row = data[i];
      var status = (row[COL_STATUS - 1] || '').toString().trim();
      var messageId = (row[COL_MESSAGE_ID - 1] || '').toString().trim();

      // Skip if no Message ID (treat as invalid; mark IGNORED to avoid reprocessing)
      if (!messageId) {
        updates.push([i + 1, 'IGNORED']);
        continue;
      }
      // Skip if already processed (Sent = row sent to Jira; Jira issue stays To Do until moved there)
      if (status === 'Sent' || status === 'DONE' || status === 'Duplicate' || status.indexOf('ERROR') === 0 || status === 'IGNORED') {
        continue;
      }

      // Deduplication: same Message ID already in sheet?
      var isDuplicate = false;
      for (var j = 1; j < data.length; j++) {
        if (j === i) continue;
        var otherId = (data[j][COL_MESSAGE_ID - 1] || '').toString().trim();
        var otherStatus = (data[j][COL_STATUS - 1] || '').toString().trim();
        if (otherId === messageId && (otherStatus === 'Sent' || otherStatus === 'DONE' || otherStatus.indexOf('ERROR') === 0)) {
          isDuplicate = true;
          break;
        }
      }
      if (isDuplicate) {
        updates.push([i + 1, 'Duplicate']);
        continue;
      }

      // Build payload: crisp summary (first sentence, no fluff), description with proper bullets
      var summary = crispSummary(row[COL_SUMMARY - 1] || '');
      var description = sanitizeForJira(row[COL_DESCRIPTION - 1] || '') || messageId;
      var assigneeEmail = (row[COL_ASSIGNEE - 1] || '').toString().trim();

      var payload = {
        summary: summary,
        description: description,
        assigneeEmail: assigneeEmail,
        labels: ['Injected']
      };

      var props = PropertiesService.getScriptProperties();
      var jiraUrl = props.getProperty('JIRA_URL');
      var jiraSecret = props.getProperty('JIRA_SECRET_KEY');
      if (!jiraUrl || !jiraSecret) {
        updates.push([i + 1, 'ERROR: Script properties JIRA_URL and JIRA_SECRET_KEY must be set.']);
        continue;
      }

      var options = {
        method: 'post',
        contentType: 'application/json',
        payload: JSON.stringify(payload),
        headers: {
          'X-Automation-Webhook-Token': jiraSecret
        },
        muteHttpExceptions: true
      };

      var response;
      try {
        response = UrlFetchApp.fetch(jiraUrl, options);
      } catch (err) {
        updates.push([i + 1, 'ERROR: ' + (err.message || 'Request failed')]);
        continue;
      }

      var code = response.getResponseCode();
      if (code >= 200 && code < 300) {
        updates.push([i + 1, 'Sent']);
      } else {
        updates.push([i + 1, 'ERROR: ' + code]);
      }
    }

    // Batch status updates
    for (var u = 0; u < updates.length; u++) {
      sheet.getRange(updates[u][0], COL_STATUS).setValue(updates[u][1]);
    }
    if (updates.length > 0) {
      SpreadsheetApp.flush();
    }
  } finally {
    lock.releaseLock();
  }
}
