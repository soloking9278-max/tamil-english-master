# Tamil English Master — General Everyday English

## What is included
- A premium-style responsive public learning website
- `examples.json`: **10,000 bilingual sentence practice examples**
- Search English or Tamil, filter by 10 everyday topics and sentence-pattern family
- English/Tamil browser speech playback when device voices are available
- Repeat-after-me studio, daily example, quiz, favourites and local progress
- `manifest.json`, `icon.svg`, `sw.js`
- Optional scheduled GitHub Actions workflow to update `daily.json` from the example bank each day

## Example library scope
The 10,000 entries are generated from 100 paired English–Tamil action phrases and 10 sentence-pattern families with 10 contextual variants each. They are useful practice examples, not 10,000 individually authored lessons. Because some template combinations can sound less natural for certain actions, treat this as a large practice bank; future versions can replace/add reviewed phrase records.

## Publish the website online
Repository: https://github.com/soloking9278-max/tamil-english-master
Live website: https://soloking9278-max.github.io/tamil-english-master/

1. In GitHub, open the repository and choose `index.html` → pencil/Edit.
2. Replace all contents with the new `index.html` in this package and commit to `main`.
3. Use **Add file → Upload files** to upload `examples.json`, `daily.json`, `manifest.json`, `sw.js`, and `icon.svg` from the package root; commit.
4. For automatic scheduled daily update, create a new file using **Add file → Create new file**. Name it `.github/workflows/refresh-daily.yml`, then copy/paste the content from the same path inside the ZIP; commit.
5. Also create `scripts/update_daily.py` by **Add file → Create new file**, using the same path and content from the ZIP; commit.
6. In **Settings → Actions → General → Workflow permissions**, ensure the workflow can have read/write repository contents if the daily workflow reports a permission error.
7. Open the **Actions** tab and run **Refresh daily English example** once with **Run workflow**. The scheduled workflow will then update `daily.json` daily from the existing library; it does not generate new AI-written content.
8. Confirm the GitHub Pages deployment has succeeded and reload the live website with Ctrl+F5.

## Automation clarification
- Daily example rotation is automatic without any API key; users also see a date-based example if the workflow has not run.
- The GitHub Action updates the daily featured example using an existing example in `examples.json`.
- Truly new, AI-written content generated every day requires an AI provider/API and a secure server-side secret. Do not place API keys in `index.html` or any public repository.

## Privacy and limitations
- Public website: anyone with the link can use it.
- Favourites and practice progress are saved locally in the browser; there are no user accounts or cloud sync.
- Speech uses device/browser voices. Tamil audio requires a Tamil voice to be available.
- Static website/PWA-style app, not an Android APK.
- External Google Fonts improve the design when accessible; system fonts are fallback.
