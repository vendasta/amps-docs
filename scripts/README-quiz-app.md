# Kahoot-style Quiz App

Quiz with a 5-minute timer, optional mini-games after correct answers (10 sec each), and scoring. Questions are stored in a Google Sheet; learners open one web app URL to play.

---

## What’s in the repo

- **`quiz_kahoot.gs`** – Apps Script backend: serves the app, reads questions from the sheet, optional save score.
- **`Quiz.html`** – Front-end: quiz UI, 5-min timer, two mini-games (targets + catch), scoring.

---

## Features

- **Upload questions** via a Google Sheet (no code to edit).
- **5-minute** total quiz time; countdown shown on screen.
- **Scoring:** 100 points per correct answer + bonus from mini-games (10 per target click, 10 per catch).
- **After each correct answer:** a random mini-game runs for **10 seconds**:
  - **Targets:** Click the orange circles that appear; each click = +10.
  - **Catch:** Move the mouse to move the paddle; catch green falling blocks; each catch = +10.
- **Optional leaderboard:** Save scores to a "Scores" sheet (name + total + quiz points + game points).

---

## Sheet structure

Create a Google Sheet (or use an existing one) and add a tab named **Questions**.

### Tab: **Questions**

| A | B | C | D | E | F |
|---|----|----|----|---|---|
| **Question** | **Option A** | **Option B** | **Option C** | **Option D** | **Correct** |
| What is 2+2? | 3 | 4 | 5 | 6 | B |
| Capital of France? | London | Berlin | Paris | Madrid | C |

- **Column A:** Question text.
- **Columns B–E:** Answer options (A, B, C, D).
- **Column F:** Correct answer — exactly **A**, **B**, **C**, or **D** (case doesn’t matter).

Row 1 = headers; from row 2 onward, one row per question.

### Tab: **Scores** (optional)

Created automatically when someone clicks “Save score” after the quiz. Columns: Timestamp, Name, Total Score, Quiz Points, Game Points.

---

## Setup

### 1. Create the Sheet and questions

1. Create a new Google Sheet (or use an existing one).
2. Add a tab named **Questions**.
3. Row 1: headers as in the table above.
4. From row 2, add your questions (Question, Option A–D, Correct).

### 2. Add the script and HTML

1. In the same Google Sheet: **Extensions → Apps Script**.
2. **Backend:** Add a new script file (e.g. name it **quiz_kahoot**). Open **`quiz_kahoot.gs`** from this repo, copy all contents, paste into that file, **Save**.
3. **Front-end:** In the Apps Script project, click **+** next to Files → **HTML**. Name the file **Quiz** (exactly). Open **`Quiz.html`** from this repo, copy all contents, paste into the Quiz file (replace any placeholder), **Save**.

### 3. Deploy as web app

1. In Apps Script: **Deploy → New deployment**.
2. Click the gear icon next to “Select type” → **Web app**.
3. **Description:** e.g. “Quiz app”.
4. **Execute as:** Me (your account).
5. **Who has access:** e.g. “Anyone” (so learners can open the link without signing in), then **Deploy**.
6. Copy the **Web app URL** and share it with learners.

### 4. Test

1. Open the Web app URL in a browser.
2. You should see “Loading questions...” then the first question and a 5:00 timer.
3. Pick an answer, click **Submit**. If correct, a 10-second mini-game (targets or catch) runs, then the next question.
4. Let the timer run or answer all questions; at the end you see total score and can enter a name and save score.

---

## Quick reference

| Item | Value |
|------|--------|
| Questions sheet tab name | `Questions` |
| Columns | A=Question, B=Option A, C=Option B, D=Option C, E=Option D, F=Correct (A/B/C/D) |
| Points per correct answer | 100 |
| Mini-game duration | 10 seconds |
| Points per target click / catch | 10 |
| Total quiz time | 5 minutes |
| HTML file name in Apps Script | **Quiz** (must match `createTemplateFromFile('Quiz')`) |

---

## Troubleshooting

- **“No questions found”:** Ensure the sheet has a tab named **Questions**, headers in row 1, and at least one data row from row 2. Column F must be A, B, C, or D.
- **Blank or broken page:** Ensure the HTML file is named **Quiz** (capital Q) in the Apps Script project and that **doGet** is deployed as a web app.
- **Timer or games feel off:** Use a modern browser (Chrome/Edge/Firefox). Avoid leaving the tab in the background for long during the quiz.
