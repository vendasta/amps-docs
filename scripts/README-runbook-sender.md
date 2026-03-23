# Runbook / Checklist Sender

Get the full checklist for a process (e.g. SEO Audit, GBP Creation) by email or from the sheet. Standalone — does not change Jira or any existing automation.

---

## What’s in the repo

- **`runbook_sender.gs`** – Apps Script to paste into your Google Sheet’s Apps Script project.

---

## How it works (simple)

1. On the **Runbook** tab, the user **types what they want** in **column A** (e.g. “seo audit”, “gbp”, “website build”). No dropdown — they type freely.
2. The **answer** (full checklist) appears **directly in the sheet** in **column B**. The script matches their text to a process (e.g. “seo” matches “SEO Audit (First 1–3 days)”) and fills B2. When they edit A2, B2 updates automatically (or use **Runbook → Show checklist in sheet**).
3. **Optional:** To email the checklist, put an address in **C2** and use **Runbook → Send checklist to email (uses C2)**.

---

## Where the checklist data comes from (pick what fits you)

You don’t have to type checklists into the Runbook sheet. You can:

### Option A: Pull from the sheet where you already have everything

If you already have a Google Sheet with process names and checklists (or URLs), point the script at it:

1. Add a tab named **Config** to your Runbook Sender sheet.
2. In **Config**, set:
   - **A1:** `Source Spreadsheet ID`  
     **A2:** Paste the **ID** of the spreadsheet that has your data.  
     (Open that sheet → look at the URL: `https://docs.google.com/spreadsheets/d/**THIS_PART**/edit` — that’s the ID.)
   - **B1:** `Source Tab Name`  
     **B2:** The exact name of the tab that has your list (e.g. `SOPs`, `Checklists`, `Process List`).
3. In that **other** sheet, the tab should have at least: **Column A** = Process name, **Column B** = Checklist text or a URL (see Option B).

The script will read process names and checklists from that spreadsheet and tab. No copy-paste into the Runbook sheet.

### Option B: Pull from the repo (or any URL) automatically

If your SOPs live in the repo (e.g. markdown files) or on a docs site:

- In the checklist column (**B**), put a **URL** instead of text:
  - **GitHub raw file:**  
    `https://raw.githubusercontent.com/YOUR_ORG/amps-docs/main/docusaurus/docs/sop/seo-services.md`
  - **Any public URL** that returns markdown or HTML (the script will strip formatting and use the content).

When someone requests that process, the script **fetches the URL**, converts the content to plain text, and emails it. No need to copy the doc into the sheet — just the link.

You can **combine** A and B: use Config to point to your existing sheet, and in that sheet put URLs in column B for some rows and plain checklist text for others.

---

## Setup

### 1. Create a Google Sheet (or use an existing one)

- Create a new Google Sheet (recommended so nothing else is affected).
- Name it e.g. **Runbook Sender**.

### 2. Where to put your process list

- **If you use your own sheet (Option A above):** Add a tab named **Config**, set A2 = that sheet’s ID and B2 = that sheet’s tab name. No need for a “Checklists” tab in the Runbook sheet unless you want a local copy too.
- **If you use this sheet:** Add a tab named **Checklists**. Row 1: **A1** = `Process Name`, **B1** = `Checklist`, **C1** = `Doc URL (optional)`. From row 2 onward:
  - **Column A:** Process name.
  - **Column B:** Either the full checklist text **or** a URL (e.g. GitHub raw `.md` link) to pull from the repo automatically.
  - **Column C:** (Optional) Link to the full SOP doc.

If no source sheet is configured and the **Checklists** tab is empty, the script uses three built-in checklists (SEO Audit, GBP Creation, Express Website Build).

### 3. Add the script

1. In the Google Sheet: **Extensions → Apps Script**.
2. If you see `Code.gs`, rename it to `runbook_sender` (right‑click → Rename), or add a new file and name it `runbook_sender`.
3. Open **`runbook_sender.gs`** from this repo, copy **all** of its contents, paste into the Apps Script editor (replace any existing code in that file), then **Save** (Ctrl+S).

### 4. Use it from the sheet

1. Add a tab named **Runbook** (or use the first sheet).
2. Set up the Runbook tab:
   - **A1:** `Type what you need (e.g. seo audit, gbp, website build)`
   - **B1:** `Checklist (answer appears here)`
   - **C1:** (optional) `Email` — only if you want to use “Send to email” later.
3. Leave **A2** and **B2** empty. The user types in **A2**; the script writes the checklist in **B2** (no dropdown).
4. Reload the spreadsheet. You should see the **Runbook** menu.
5. **To get the answer:** User **types** in **A2** (e.g. “seo audit”, “gbp”, “bing”). The checklist appears in **B2** automatically when they finish editing A2, or they can use **Runbook → Show checklist in sheet (A2 → B2)**. No email needed. Matching is case-insensitive and partial (e.g. “seo” matches “SEO Audit (First 1–3 days)”).

---

## Optional: Use a Google Form

If you want people to request a checklist by form (they pick process and enter email, and get the checklist by email):

1. **Create a form** (Google Forms) with two questions:
   - **Question 1:** “Which process?” → **Dropdown** or **List**. Add the same options as your process names (e.g. copy from the Checklists sheet: SEO Audit (First 1–3 days), GBP Creation & Claiming, etc.).
   - **Question 2:** “Your email” → **Short answer** (or “Email” type if available).
2. **Link the form to the same spreadsheet:** Form → **Responses** → **Link to Sheets** → select the Runbook Sender sheet. This creates a new tab (e.g. “Form Responses 1”) with columns: Timestamp, Which process?, Your email.
3. **Add the trigger in Apps Script:**
   - In Apps Script: **Triggers** (clock icon) → **+ Add Trigger**.
   - Function: **onFormSubmit**
   - Event: **From spreadsheet** → **On form submit**
   - Save and authorize if asked.
4. When someone submits the form, the script runs and emails the checklist to the email they entered.

**Note:** If your form has more than two questions, open `runbook_sender.gs` and in `onFormSubmit` adjust the indices: `e.values[1]` is the first form response (after timestamp), `e.values[2]` is the second. So keep “Which process?” first and “Your email” second, or change the indices to match your column order.

---

## Example rows for the “Checklists” sheet

You can paste these into **Checklists** (row 2 onward) or use them as a template. The script already has these three as built-ins if the sheet is empty; putting them in the sheet lets you edit the text.

| Process Name | Checklist | Doc URL (optional) |
|--------------|-----------|--------------------|
| SEO Audit (First 1–3 days) | Same business day: • Complete Admin Work (CE): Audit Fulfillment Form, Send Confirmation Email … (rest of checklist in one cell) | https://your-docs-site.com/sop/seo-services |
| GBP Creation & Claiming | Core rules: • Log in to business.google.com … (full checklist in one cell) | https://your-docs-site.com/sop/gbp-creation-claiming |
| Express Website Build (Divi) – Key steps | Admin: Team Lead assigns … (key steps in one cell) | https://your-docs-site.com/sop/express-website-build-divi |

For **Checklist**, you can use multiple lines and bullets in the same cell (use Alt+Enter for new lines in the cell).

---

## Quick reference

- **Config tab (optional):** A2 = Source Spreadsheet ID (the sheet where you have all the info), B2 = Source Tab name. Leave blank to use the “Checklists” tab in this sheet.
- **Checklists / your source tab:** Process Name (A), Checklist text or **URL** (B), Doc URL (C). If B is a URL, the script fetches content from the repo/docs automatically.
- **Runbook tab:** A2 = **user types** what they want (e.g. seo audit, gbp) — **this is the “question”**; B2 = checklist (answer appears here, no email); C2 = optional email if you use “Send to email.”
- **Runbook → Show checklist in sheet (A2 → B2):** Matches the text in A2 to a process and writes the checklist in B2. B2 often updates automatically when A2 is edited.
- **Runbook → Refresh process list from source:** Only needed if you use Config and want a ProcessList tab; not required for the type-in-A2 flow.
- **Form (optional):** First question = process, second = email. Trigger: On form submit → `onFormSubmit`.
- **Permissions:** The script needs access to the spreadsheet(s), Gmail (to send email), and (if you use URLs) the internet to fetch checklist content. It does not touch Jira or your Requests sheet.

---

## Hackathon demo tip

1. Show the **Checklists** tab with 2–3 processes.
2. On the **Runbook** tab, pick “SEO Audit” and your email, then run **Runbook → Send checklist to email in B2**.
3. Open your inbox and show the checklist email.
4. Optional: Show the form and submit once; then show that the same checklist was emailed from the form.

This demonstrates “one click (or one form submit) = full runbook in your inbox” without touching existing automation.
