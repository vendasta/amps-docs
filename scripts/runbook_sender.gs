/**
 * Runbook / Checklist Sender - Apps Script
 *
 * Lets users pick a process and get the full checklist by email. Does not touch Jira.
 *
 * DATA SOURCE (pick one or combine):
 * - Pull from YOUR existing sheet: use the "Config" tab to point to another spreadsheet
 *   and tab where you already have Process Name | Checklist (or URL).
 * - Pull from repo/docs: in the checklist column put a URL (e.g. GitHub raw .md or docs
 *   page); the script will fetch and use that content as the checklist.
 *
 * SETUP: See README. Config tab (optional): A2 = Source Spreadsheet ID, B2 = Source Tab Name.
 */

const CHECKLIST_SHEET_NAME = 'Checklists';
const RUNBOOK_SHEET_NAME = 'Runbook';
const CONFIG_SHEET_NAME = 'Config';
const DEFAULT_PROCESS_COL = 1;  // A
const DEFAULT_CHECKLIST_COL = 2;
const DEFAULT_LINK_COL = 3;
const URL_FETCH_TIMEOUT_MS = 15000;

/**
 * Gets the spreadsheet and sheet to read checklists from. Uses Config tab if present:
 * - Config A2 = Source Spreadsheet ID (optional). If set, open that spreadsheet.
 * - Config B2 = Source Tab name (optional). If empty, use "Checklists".
 * Returns { spreadsheet, sheet } or { spreadsheet, sheet: null } if tab not found.
 */
function getChecklistSource() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sourceId = null;
  var tabName = CHECKLIST_SHEET_NAME;
  var configSheet = ss.getSheetByName(CONFIG_SHEET_NAME);
  if (configSheet) {
    try {
      var a2 = configSheet.getRange('A2').getValue();
      var b2 = configSheet.getRange('B2').getValue();
      if (a2 && a2.toString().trim()) sourceId = a2.toString().trim();
      if (b2 && b2.toString().trim()) tabName = b2.toString().trim();
    } catch (e) {}
  }
  var spreadsheet = sourceId ? SpreadsheetApp.openById(sourceId) : ss;
  var sheet = spreadsheet.getSheetByName(tabName);
  return { spreadsheet: spreadsheet, sheet: sheet };
}

/**
 * Fetches content from a URL and converts to plain-text checklist (strips markdown or HTML).
 */
function fetchChecklistFromUrl(url) {
  if (!url || !url.toString().trim()) return null;
  var u = url.toString().trim();
  if (u.indexOf('http://') !== 0 && u.indexOf('https://') !== 0) return null;
  try {
    var response = UrlFetchApp.fetch(u, { muteHttpExceptions: true, timeout: URL_FETCH_TIMEOUT_MS });
    if (response.getResponseCode() !== 200) return null;
    var raw = response.getContentText();
    if (!raw) return null;
    // Markdown: strip front matter, convert ## to bold section, * to bullet, remove links
    if (raw.indexOf('---') === 0) {
      var end = raw.indexOf('---', 3);
      if (end !== -1) raw = raw.substring(end + 3);
    }
    raw = raw.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');
    raw = raw.replace(/#{1,6}\s*/g, '\n');
    raw = raw.replace(/\*\*([^*]+)\*\*/g, '$1');
    raw = raw.replace(/\*([^*]+)\*/g, '$1');
    raw = raw.replace(/^\s*[-*]\s+/gm, '• ');
    raw = raw.replace(/^\s*\d+\.\s+/gm, '');
    raw = raw.replace(/<[^>]+>/g, '');
    raw = raw.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
    raw = raw.replace(/\n{3,}/g, '\n\n').trim();
    return raw;
  } catch (e) {
    return null;
  }
}

/** Default checklists if no sheet data and no URL (paste your own into the Sheet to override). */
function getDefaultChecklists() {
  return {
    'SEO Audit (First 1–3 days)': [
      'Same business day:',
      '• Complete Admin Work (CE): Audit Fulfillment Form, Send Confirmation Email',
      '',
      'Within 1–3 days:',
      '• Perform Competitive Analysis (identify 3–5 competitors, document strengths/weaknesses)',
      '• Audit client website (crawl with SERanking, check structure, content, technical SEO)',
      '• Research & finalize keyword set (volume, competition, primary/secondary/long-tail)',
      '• Establish baseline rank for keyword set (SERanking, document date/time)',
      '• Create initial slide deck (findings, keyword strategy, example: Ganbatte SEO Consultation Report)',
      '• Send post-consult email',
    ].join('\n'),
    'GBP Creation & Claiming': [
      'Core rules:',
      '• Log in to business.google.com with your personal email',
      '• Select correct Organization from top-left before any action',
      '• Use 10-digit Group ID (not email) when requesting access',
      '• NEVER claim from Google Search "Own this business?" — use Organization flow only',
      '',
      'Create new listing:',
      '1. Select correct Organization → Profile Group',
      '2. Add Business → Add a single business',
      '3. Follow prompts; verify or complete verification flow',
      '',
      'Request access to existing listing:',
      '1. Get 10-digit Group ID for the brand',
      '2. Instruct client: Business Profile settings → People and access → Add → paste Group ID',
      '3. Accept from Organization account',
    ].join('\n'),
    'Express Website Build (Divi) – Key steps': [
      'Admin: Team Lead assigns Developer/QA, process order',
      'Backend: Launch WordPress Hosting Pro, update everything, plugin settings',
      'Front-end: Divi theme options, Theme Builder footer, Customizer, generate site with AI',
      'Content: Business & project info, structure & content directives, CRM forms',
      'Revisions: Send first mock, receive revisions, set second mock due date, complete revisions',
      'Handoff: Final settings, last tasks, transition to Website Support',
    ].join('\n'),
  };
}

/**
 * Returns the checklist text for a process name. Reads from your configured source sheet
 * (or "Checklists" tab). If the checklist cell is a URL, fetches content from repo/docs.
 */
function getChecklistForProcess(processName) {
  if (!processName || !processName.toString().trim()) return null;
  var key = processName.toString().trim();
  var source = null;
  try {
    source = getChecklistSource();
  } catch (e) {
    return getDefaultChecklists()[key] || null;
  }
  if (source.sheet) {
    var data = source.sheet.getDataRange().getValues();
    if (data.length > 1) {
      for (var i = 1; i < data.length; i++) {
        if (data[i][DEFAULT_PROCESS_COL - 1] && data[i][DEFAULT_PROCESS_COL - 1].toString().trim() === key) {
          var cellB = data[i][DEFAULT_CHECKLIST_COL - 1] ? data[i][DEFAULT_CHECKLIST_COL - 1].toString().trim() : '';
          var text = '';
          if (cellB.indexOf('http://') === 0 || cellB.indexOf('https://') === 0) {
            text = fetchChecklistFromUrl(cellB) || ('(Could not load from URL: ' + cellB + ')');
          } else {
            text = cellB;
          }
          var link = (data[i][DEFAULT_LINK_COL - 1] && data[i][DEFAULT_LINK_COL - 1].toString().trim()) ? data[i][DEFAULT_LINK_COL - 1].toString().trim() : '';
          if (link) text = text + '\n\nFull doc: ' + link;
          return text;
        }
      }
    }
  }
  return getDefaultChecklists()[key] || null;
}

/**
 * Finds a process name that matches what the user typed (case-insensitive, "contains").
 * e.g. "seo" or "seo audit" matches "SEO Audit (First 1–3 days)".
 * Returns the matching process name or null.
 */
function findMatchingProcess(userInput) {
  if (!userInput || !userInput.toString().trim()) return null;
  var typed = userInput.toString().trim().toLowerCase();
  var list = getProcessList();
  for (var i = 0; i < list.length; i++) {
    var name = list[i].toLowerCase();
    if (name.indexOf(typed) >= 0 || typed.indexOf(name) >= 0) return list[i];
  }
  return null;
}

/**
 * Returns list of process names (from your source sheet column A or default keys).
 */
function getProcessList() {
  try {
    var source = getChecklistSource();
    if (source.sheet) {
      var data = source.sheet.getDataRange().getValues();
      if (data.length > 1) {
        var list = [];
        for (var i = 1; i < data.length; i++) {
          var name = data[i][DEFAULT_PROCESS_COL - 1] ? data[i][DEFAULT_PROCESS_COL - 1].toString().trim() : '';
          if (name) list.push(name);
        }
        if (list.length > 0) return list;
      }
    }
  } catch (e) {}
  return Object.keys(getDefaultChecklists());
}

/**
 * Sends the checklist for the given process to the given email.
 * Returns { success: boolean, message: string }.
 */
function sendChecklistToEmail(processName, toEmail) {
  if (!toEmail || !toEmail.toString().trim()) {
    return { success: false, message: 'Please enter an email address.' };
  }
  var checklist = getChecklistForProcess(processName);
  if (!checklist) {
    return { success: false, message: 'No checklist found for "' + processName + '". Check the process name or add it to the Checklists sheet.' };
  }
  var subject = 'Runbook: ' + processName;
  var body = 'Hi,\n\nHere is your checklist for: ' + processName + '\n\n---\n\n' + checklist + '\n\n---\n(Sent from Runbook Sender)';
  try {
    GmailApp.sendEmail(toEmail.toString().trim(), subject, body);
    return { success: true, message: 'Checklist sent to ' + toEmail + '.' };
  } catch (e) {
    return { success: false, message: 'Could not send email: ' + e.toString() };
  }
}

/**
 * Shows the checklist directly in the sheet: user types in A2 (e.g. "seo audit"), script
 * finds the matching process and writes the checklist into B2. No dropdown, no email.
 */
function showChecklistInSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(RUNBOOK_SHEET_NAME) || ss.getSheets()[0];
  var userInput = sheet.getRange('A2').getValue();
  if (!userInput || !userInput.toString().trim()) {
    sheet.getRange('B2').clearContent();
    sheet.getRange('B2').setValue('(Type what you need in column A, e.g. seo audit, gbp, website build)');
    return;
  }
  var processName = findMatchingProcess(userInput);
  if (!processName) {
    var available = getProcessList().join(', ');
    sheet.getRange('B2').setValue('No checklist found for "' + userInput + '". Try: ' + available);
    return;
  }
  var checklist = getChecklistForProcess(processName);
  if (!checklist) {
    sheet.getRange('B2').setValue('No checklist found for: ' + processName);
    return;
  }
  sheet.getRange('B2').setValue(checklist);
}

/**
 * Run from Sheet: reads process from A2 and email from C2, then sends email (optional).
 * B2 is used for the checklist display, so email is in C2 if you use "Send to email".
 */
function sendChecklistFromSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(RUNBOOK_SHEET_NAME) || ss.getSheets()[0];
  var processName = sheet.getRange('A2').getValue();
  var toEmail = sheet.getRange('C2').getValue();
  var result = sendChecklistToEmail(processName, toEmail);
  if (result.success) {
    SpreadsheetApp.getUi().alert('Done', result.message, SpreadsheetApp.getUi().ButtonSet.OK);
  } else {
    SpreadsheetApp.getUi().alert('Error', result.message, SpreadsheetApp.getUi().ButtonSet.OK);
  }
}

/**
 * Form submit trigger: use this as the trigger function when the linked form is submitted.
 * Form should have: Question 1 = Process (dropdown), Question 2 = Your email (text).
 * Install trigger: From spreadsheet → On form submit → onFormSubmit
 */
function onFormSubmit(e) {
  if (!e || !e.values || e.values.length < 2) return;
  var processName = e.values[1];   // first data column after timestamp
  var toEmail = e.values[2] || ''; // second data column (adjust indices if your form has more questions)
  if (!toEmail || !toEmail.toString().trim()) return;
  var result = sendChecklistToEmail(processName, toEmail);
  if (!result.success) {
    Logger.log('Runbook send failed: ' + result.message);
  }
}

/**
 * Refreshes the process list from your source (Config sheet or Checklists). Writes names to
 * a tab named "ProcessList" (creates it if needed), column A. Use data validation
 * "List from range" = ProcessList!A2:A on the Runbook tab so the dropdown stays in sync.
 */
function refreshProcessList() {
  var names = getProcessList();
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('ProcessList');
  if (!sheet) {
    sheet = ss.insertSheet('ProcessList');
  }
  sheet.clear();
  sheet.getRange(1, 1).setValue('Process Name');
  if (names.length > 0) {
    sheet.getRange(2, 1, 1 + names.length, 1).setValues(names.map(function (n) { return [n]; }));
  }
  SpreadsheetApp.getUi().alert('Done', 'Process list refreshed (' + names.length + ' processes). Use dropdown range: ProcessList!A2:A', SpreadsheetApp.getUi().ButtonSet.OK);
}

/**
 * When the user changes A2 on the Runbook sheet (e.g. selects from dropdown), show the
 * checklist in B2 automatically. This is how the "question" (selection in A2) is captured.
 * Install trigger: Edit → Current project's triggers → Add trigger →
 *   Function: onEdit, Event: From spreadsheet, On edit.
 */
function onEdit(e) {
  if (!e || !e.range) return;
  var sheet = e.range.getSheet();
  if (sheet.getName() !== RUNBOOK_SHEET_NAME) return;
  if (e.range.getRow() !== 2 || e.range.getColumn() !== 1) return;
  showChecklistInSheet();
}

/**
 * Add custom menu when the spreadsheet opens.
 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Runbook')
    .addItem('Show checklist in sheet (A2 → B2)', 'showChecklistInSheet')
    .addItem('Send checklist to email (uses C2)', 'sendChecklistFromSheet')
    .addItem('Refresh process list from source', 'refreshProcessList')
    .addToUi();
}
