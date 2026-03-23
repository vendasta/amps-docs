# VS Internal Bot – Architecture diagrams (non-ASCII)

Use these in any tool that supports **Mermaid** (e.g. GitHub, GitLab, Confluence with Mermaid macro, [Mermaid Live Editor](https://mermaid.live), or export to PNG/SVG).

---

## 1. Knowledge flow (source to users)

```mermaid
flowchart LR
  A[Guru Cards\n(source)] -->|export/update| B[AMPS Docs\n(published site)]
  B -->|knowledge links| C[VS Internal Bot\n(Chat Receptionist)]
  C -->|answers| D[Google Chat\n(VS Internal)]
```

---

## 2. Feedback flow (flag wrong answer → fix at source)

```mermaid
flowchart TB
  U[User reacts 🎫 on wrong answer in Google Chat]
  U --> S[Feedback/requests\nGoogle Sheet]
  S -->|automation\n(new row → task)| J[Jira board (CJT)]
  J -->|assign & fix\n(update AMPS Docs and/or Guru)| K[Knowledge owners\n(update source)]
```

---

## How to use

- **In GitHub/GitLab:** Paste the contents of a code block into a `.md` file inside a ` ```mermaid ` block; the diagram will render.
- **Export as image:** Go to [mermaid.live](https://mermaid.live), paste the Mermaid code, then use **Actions → PNG/SVG** to download.
- **In Confluence:** Use the Mermaid macro (or a “Diagram” app that supports Mermaid) and paste the code.
- **In Word:** Export from Mermaid Live as PNG, then insert the image into your document.
