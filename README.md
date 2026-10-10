# Tamil English Master — Premium Public Website

This package is a browser-based static website intended for public use through GitHub Pages. No software installation is required to publish or use it.

## Included
- `index.html` — responsive premium-style learning interface
- `manifest.json` — PWA metadata
- `sw.js` — service worker/offline app shell cache
- `icon.svg` — app icon

## Publish online
Repository: https://github.com/soloking9278-max/tamil-english-master
Live site: https://soloking9278-max.github.io/tamil-english-master/

1. Open your GitHub repository.
2. Click `index.html`, then the pencil/edit icon.
3. Replace the whole file with the contents of this package's `index.html`.
4. Click **Commit changes** on the `main` branch.
5. Choose **Add file → Upload files** and upload `manifest.json`, `sw.js`, and `icon.svg`; commit the upload.
6. Open the live site and refresh with Ctrl+F5. If an older cached copy remains, close the site tab and reopen it after the new Pages deployment succeeds.

## Public access and privacy
- The GitHub Pages URL is public: anyone with the link can access the site without an account or installation.
- Progress data is stored locally in each visitor's browser. Visitors do not share progress or personal data with one another.
- A shared account, cross-device cloud progress, real voice recording/evaluation, admin dashboard, or paid membership would require a backend/authentication service; those are not included.
- Speech playback uses the voices exposed by the visitor's browser/device. Tamil playback requires an available Tamil voice; English voice choices also vary.
- This is a static PWA-style website, not an Android APK. On supported devices, a visitor may use the browser's “Add to Home Screen” feature.
- The module cards display the course roadmap. Lesson 1 and practice/quiz features are currently implemented; roadmap labels are not a claim that all future lessons have been built.
- Google Fonts are requested for visual polish; system fonts provide a fallback if external fonts are blocked.
