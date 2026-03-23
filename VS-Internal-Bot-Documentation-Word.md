# VS Internal Bot: Knowledge Base and Feedback Loop

**Document version:** 1.0  
**Last updated:** March 2026

---

## 1. Overview

This document describes the end-to-end process for:

1. **Knowledge sourcing and delivery** — Exporting content from Guru cards, publishing SOPs and knowledge in the AMPS Docs repository, connecting that knowledge to the **Chat Receptionist – VS Internal Bot**, and having the bot answer user queries in Google Chat.
2. **Feedback and correction loop** — Allowing users to flag incorrect or contradictory bot responses by reacting with the ticket emoji (🎫). That reaction creates a row in a Google Sheet, which triggers creation of a Jira task. Tasks are assigned to knowledge owners to update the source content, keeping the bot's knowledge accurate over time.

**Goals:** Single source of truth (AMPS Docs); answers in Google Chat from the VS Internal Bot; incorrect answers captured and fixed at the source via Sheet and Jira.

---

## 2. Architecture and Diagrams

**Figure 1 – Architecture:** Guru Cards → (export/update) → AMPS Docs (published site) → (knowledge links) → Chat Receptionist – VS Internal Bot → (answers) → Google Chat. Feedback: User reacts 🎫 → Google Sheet (new row) → Jira board (new task) → Owners update knowledge source.

**Figure 2 – Feedback loop:** (1) User reacts 🎫 in Google Chat on wrong answer → (2) New row on Sheet → (3) New task on Jira (CJT) → (4) Assigned to owners → (5) Owners update AMPS Docs/Guru → Bot answers correctly.

*Diagrams generated: VS-Internal-Bot-Architecture.png and VS-Internal-Bot-Feedback-Loop.png. Copy them from your Cursor project assets folder into this repo (e.g. docs/images/) and insert into Confluence.*

---

## 3. Part 1: Knowledge Base Setup and Bot Answers

### 3.1 From Guru Cards to AMPS Docs

Content was exported from **Guru cards** and used to create or update **SOPs and knowledge articles** in the **AMPS Docs** repository. The repository is built and published as a documentation site.

**Published knowledge base (AMPS Docs):**  
https://amps-docs-642433220657.us-central1.run.app/docs/intro

This site is the **single source of truth** for the procedures and knowledge that the bot uses.

### 3.2 Connecting Knowledge to the Bot

The **Chat Receptionist – VS Internal Bot** is configured in Vendasta's Business App (AI Assistants). **Knowledge links** pointing to the AMPS Docs site were added to this bot.

**Bot configuration (Vendasta – sign-in required):**  
https://vendasta-corporate-only.smblogin.com/account/location/AG-4JSWHQFDFW/ai/assistants/ASSISTANT-chat-receptionist/edit

### 3.3 Where Users Get Answers

Users ask questions about **SOPs and Guru card knowledge** in the **VS Internal Google Chat space**. The **VS Internal Bot** responds there using the knowledge linked from AMPS Docs.

**Google Chat space (VS Internal):**  
https://chat.google.com/room/AAAAbYrLTAc?cls=7

---

## 4. Part 2: Feedback Loop

### 4.1 User flags a wrong or contradicting answer

When a user sees a **bot response** that is **incorrect** or **contradicts** known procedures/SOPs, they **react to that chat message** with the **🎫 (ticket) emoji**.

### 4.2 New row on the Google Sheet

That reaction is processed so that a **new row** is created on the **feedback/requests** Google Sheet.

**Google Sheet (feedback/requests):**  
https://docs.google.com/spreadsheets/d/1V0Gj23HD3BrUhj3QqkKFKFElkfuoSfu7RmZGTIsTsnM/edit?gid=0#gid=0

### 4.3 New task on the Jira board

When a new row is added, automation (Apps Script + Jira webhook) **creates a new task** on the **Chat-Jira Test (CJT)** Jira board.

**Jira board (CJT):**  
https://vendasta.jira.com/jira/software/projects/CJT/boards/1790?jql=

### 4.4 Assignment and update of knowledge

Tasks are **assigned to the existing knowledge owners** on the board. Owners **update the knowledge source** (AMPS Docs and/or Guru) so the bot responds correctly to similar questions in the future.

---

## 5. Tools and Links Reference

| Purpose | Link |
|--------|------|
| **Published knowledge base (AMPS Docs)** | https://amps-docs-642433220657.us-central1.run.app/docs/intro |
| **Chat Receptionist – VS Internal Bot (edit)** | https://vendasta-corporate-only.smblogin.com/account/location/AG-4JSWHQFDFW/ai/assistants/ASSISTANT-chat-receptionist/edit |
| **Google Chat space (VS Internal)** | https://chat.google.com/room/AAAAbYrLTAc?cls=7 |
| **Feedback / requests Google Sheet** | https://docs.google.com/spreadsheets/d/1V0Gj23HD3BrUhj3QqkKFKFElkfuoSfu7RmZGTIsTsnM/edit?gid=0#gid=0 |
| **Jira board (CJT)** | https://vendasta.jira.com/jira/software/projects/CJT/boards/1790?jql= |

---

## 6. Summary

- **Knowledge flow:** Guru → AMPS Docs (repo + published site) → knowledge links in Chat Receptionist – VS Internal Bot → answers in Google Chat.
- **Feedback flow:** User reacts 🎫 on wrong answer → row in Sheet → task in Jira (CJT) → owners update knowledge → bot responds correctly.

This keeps the VS Internal Bot aligned with current SOPs and Guru knowledge and ensures corrections are tracked and applied at the source.
