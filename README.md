# Tamil English Master — General English, diverse examples

This update addresses the repetitive pattern feel in the first generated library. It contains **10,000 unique English sentence strings** based on 100 everyday actions and 100 broader sentence frames across preferences, requests, needs, plans, conditions, habits, reflections, questions and everyday situations.

The examples are still pattern-generated practice sentences, not 10,000 individually edited lessons. Some Tamil translations may need human review; use these to practise patterns and phrases, and continue improving the library over time.

## Files to upload to GitHub root
- `index.html`
- `examples.json`
- `daily.json`
- `manifest.json`
- `icon.svg`
- `sw.js`

## Files that must be in the correct subfolders
- `scripts/update_daily.py`
- `.github/workflows/refresh-daily.yml`

## Publish
1. Replace existing root files with the copies from this package.
2. Create/replace the two subfolder files at the exact paths above (do not leave only root-level copies).
3. Commit to `main`, then go to Actions and run **Refresh daily English example**.
4. Wait for Pages deployment. Open the website and press Ctrl+F5; if needed, close the tab and reopen to load the new service-worker cache.

## Daily content behaviour
The page now reads `daily.json`'s `date` and nested `example` correctly. The workflow selects a deterministic example for each calendar date, so rerunning on the same date selects the same daily example by design. The **New example** button chooses another random example immediately.
This workflow rotates existing content; it does not call an AI service to invent new lessons.

## Public use / privacy
The website is public with no login. Favourites and progress remain in each visitor's browser. Speech depends on device voices; Tamil playback requires a Tamil voice. No cloud sync or Android APK is included.
