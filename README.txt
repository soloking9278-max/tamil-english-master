# Tamil English Master — Intermediate Update

## Files
- `index.html`: the updated app (responsive, Tamil explanations, browser text-to-speech, repeat practice, role-play, quiz, local progress).
- `manifest.json`: basic PWA metadata.
- `sw.js`: basic offline cache for the app shell.

## Important limitations
- Speech depends on voices installed/provided by the user's browser/device. Tamil audio appears only if a Tamil speech voice is available.
- Practice progress is stored in the current browser only. There is no login, cloud sync, payments, or teacher dashboard.
- This is a static website/PWA, not an Android APK. Users may be able to use browser “Add to Home Screen”.
- The course outline lists five modules; this update contains a full first lesson and a module roadmap, not a full library of lessons yet.

## Publish online without installing software
1. Open https://github.com/soloking9278-max/tamil-english-master
2. Open the existing `index.html`. Click the pencil/edit icon.
3. Replace its contents with the contents of this package's `index.html`.
4. Click **Commit changes** and commit to the branch used by Pages (usually `main`).
5. Upload `manifest.json` and `sw.js` using **Add file → Upload files**, then commit.
6. Open https://soloking9278-max.github.io/tamil-english-master/ and hard refresh (Ctrl+F5). GitHub Pages can take a few minutes to publish.

If the existing app has other files, keep them unless you know they are obsolete.
