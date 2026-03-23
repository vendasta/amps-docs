# Chat-to-Jira Apps Script

The Confluence Chat-to-Jira doc doesn’t include the script. Use this file so you can paste it into Google Apps Script.

---

## What’s in the repo

- **`chat_to_jira.gs`** – Full script to paste into your Google Sheet’s Apps Script project.

---

## How to use it

1. **Open your buffer sheet** (the one with the **Requests** tab and columns: Summary, Description, AssigneeEmail, Status, Message ID).

2. **Open Apps Script**  
   Menu: **Extensions → Apps Script**.

3. **Add the script**  
   - If you see **Code.gs**, click the ⋮ next to it → **Rename** → name it **chat_to_jira**.  
   - Open **`chat_to_jira.gs`** from this repo in a text editor, copy **all** of its contents, paste into the Apps Script editor (replace any existing code), then **Save** (Ctrl+S).

4. **Set Script Properties**  
   You need two values from Jira: the webhook **URL** and the webhook **secret**. Follow the steps in **[Where to get JIRA_URL and JIRA_SECRET_KEY in Jira](#where-to-get-jira_url-and-jira_secret_key-in-jira)** below to find them, then:
   - In Apps Script, click the **gear (Project settings)** in the left sidebar.  
   - Scroll to **Script properties** → **Add script property**.  
   - Add:
     - **Property:** `JIRA_URL`  
       **Value:** (paste the webhook URL you copied from Jira)
     - **Property:** `JIRA_SECRET_KEY`  
       **Value:** (paste the webhook secret you copied from Jira)

5. **Add the trigger**  
   - In Apps Script, click the **clock (Triggers)** in the left sidebar.  
   - **+ Add Trigger**.  
   - **Choose function:** `processSheetOnChange`  
   - **Select event source:** **From spreadsheet**  
   - **Select event type:** **On change**  
   - **Save**. Approve permissions if asked.

6. **In Jira Automation**  
   When you set up the “Create issue” action, map the webhook body to issue fields using smart values, for example:
   - Summary: `{{webhookData.summary}}`
   - Description: `{{webhookData.description}}`
   - Assignee: use the field that accepts email (e.g. assignee by email), e.g. `{{webhookData.assigneeEmail}}`
   - Labels: ensure **Injected** is applied (or map `{{webhookData.labels}}` if your rule supports it).

The script sends a JSON body like:

```json
{
  "summary": "...",
  "description": "...",
  "assigneeEmail": "...",
  "labels": ["Injected"]
}
```

So your Jira rule should reference `webhookData.summary`, `webhookData.description`, `webhookData.assigneeEmail`, and `webhookData.labels` as needed.

---

## Where to get JIRA_URL and JIRA_SECRET_KEY in Jira

Follow these steps in **Jira Cloud** (e.g. `your-site.atlassian.net` or `vendasta.jira.com`) to get the two values you need for Apps Script.

### Step 1: Open your project

1. Log in to Jira.
2. Open the project where you want Chat requests to become issues (e.g. **SRE**).

### Step 2: Go to Automation

1. Click **Project settings** (gear icon) in the left sidebar (under your project name).
2. In the project settings menu, click **Automation** (or **Automation rules**).

### Step 3: Create a new rule (or open an existing one)

1. Click **Create rule** (or **Add rule**).
2. For **Trigger**, click **Add trigger**.
3. Search for **Incoming webhook** and select it.
4. You will see:
   - A **Webhook URL** (long link starting with `https://…`).
   - A **Secret** or **Token** (shorter string).
5. Click **Copy** next to the **Webhook URL** and paste it somewhere safe (e.g. Notepad).  
   → This is your **JIRA_URL** for Script Properties.
6. Click **Copy** (or **Reveal** then copy) next to the **Secret**.  
   → This is your **JIRA_SECRET_KEY** for Script Properties.

### Step 4: Add the “Create issue” action

1. Click **Add action** (or **+ Action**).
2. Search for **Create issue** and select it.
3. Configure:
   - **Project:** your project (e.g. SRE).
   - **Issue type:** e.g. Task or Story.
   - **Summary:** click in the field → **Insert variable** or **{{** → choose **webhookData** → **summary** (so it shows `{{webhookData.summary}}`).
   - **Description:** same way, set to `{{webhookData.description}}`.
   - **Assignee:** set to `{{webhookData.assigneeEmail}}` (or use the field that accepts email).
   - **Labels:** add **Injected** (or map `{{webhookData.labels}}` if your rule supports it).
4. **Save** the rule and **Turn it on**.

### Step 5: Paste the values into Apps Script

- In Apps Script **Project settings → Script properties**:
  - **JIRA_URL** = the Webhook URL you copied in Step 3.
  - **JIRA_SECRET_KEY** = the Secret you copied in Step 3.

Do **not** share the URL or secret; treat them like passwords.

---

## Quick reference

- **Script Properties:** `JIRA_URL`, `JIRA_SECRET_KEY` (do **not** put these in the code).  
- **Trigger:** From spreadsheet → On change → `processSheetOnChange`.  
- **Sheet:** Tab name **Requests**, headers in row 1: Summary, Description, AssigneeEmail, Status, Message ID.
