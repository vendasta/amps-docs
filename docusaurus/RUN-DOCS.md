# Running the docs (same as the 11 guru cards)

## Start the site

**Normal start (port 3000):**
```bash
npm run start
```

**If you see "Can't resolve '@generated/client-modules'" or other @generated errors:**  
Clear cache and start in one step:

```bash
npm run start:dev
```

**Use port 3001:**
```bash
npm run start -- --port 3001
# or after a clear:
npm run start:dev:3001
```

Then open: **http://localhost:3000** (or **http://localhost:3001**).

## Reference: the 11 working guru cards

The following docs are the original working set (MS-Core-Services, MS-Communications, etc.). The 84 standalone guru-card docs follow the same structure:

- **Frontmatter:** `title` and `sidebar_label` (no trailing dots or semicolons)
- **Images:** under `static/img/guru/<doc-folder>/` and referenced as `![](/img/guru/.../NN.png)`
- **Sidebar:** auto-generated from the `docs` folder

If the site fails to compile, run `npm run start:dev` once to regenerate Docusaurus files and try again.
