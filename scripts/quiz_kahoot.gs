/**
 * Kahoot-style Quiz - Apps Script backend
 *
 * Serves the quiz web app and provides questions from the "Questions" sheet.
 * Sheet columns: A = Question, B = Option A, C = Option B, D = Option C, E = Option D, F = Correct (A/B/C/D)
 */

const QUESTIONS_SHEET_NAME = 'Questions';
const POINTS_CORRECT = 100;
const GAME_DURATION_SEC = 10;
const QUIZ_DURATION_SEC = 300; // 5 minutes

/**
 * Serves the quiz app when a user opens the published web app URL.
 */
function doGet() {
  return HtmlService
    .createTemplateFromFile('Quiz')
    .evaluate()
    .setTitle('Quiz')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * Returns all questions from the Questions sheet as an array of objects.
 * Called by the front-end via google.script.run.
 */
function getQuestions() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(QUESTIONS_SHEET_NAME);
  if (!sheet) return [];
  var data = sheet.getDataRange().getValues();
  if (data.length < 2) return [];
  var out = [];
  for (var i = 1; i < data.length; i++) {
    var row = data[i];
    var q = (row[0] && row[0].toString().trim()) ? row[0].toString().trim() : '';
    if (!q) continue;
    var a = (row[1] && row[1].toString().trim()) ? row[1].toString().trim() : '';
    var b = (row[2] && row[2].toString().trim()) ? row[2].toString().trim() : '';
    var c = (row[3] && row[3].toString().trim()) ? row[3].toString().trim() : '';
    var d = (row[4] && row[4].toString().trim()) ? row[4].toString().trim() : '';
    var correct = (row[5] && row[5].toString().trim()) ? row[5].toString().trim().toUpperCase() : 'A';
    if (correct !== 'A' && correct !== 'B' && correct !== 'C' && correct !== 'D') correct = 'A';
    out.push({
      question: q,
      optionA: a,
      optionB: b,
      optionC: c,
      optionD: d,
      correct: correct
    });
  }
  return out;
}

/**
 * Optional: save a score to a "Scores" sheet for leaderboard.
 * Columns: Timestamp, Name, Score, Quiz Points, Game Points
 */
function saveScore(playerName, totalScore, quizPoints, gamePoints) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Scores');
  if (!sheet) {
    sheet = ss.insertSheet('Scores');
    sheet.getRange(1, 1, 1, 5).setValues([['Timestamp', 'Name', 'Total Score', 'Quiz Points', 'Game Points']]);
  }
  sheet.appendRow([new Date(), playerName || 'Anonymous', totalScore, quizPoints, gamePoints]);
}
