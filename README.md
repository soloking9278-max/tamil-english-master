# Tamil English Master — Prototype v1

A responsive, installable web prototype that can also be wrapped as an Android app. It includes:
- 5 free beginner lessons with Tamil explanations
- English text-to-speech using the browser's speech engine, preferring a female English voice when available
- Tamil → English repeat mode: hear Tamil meaning, then English sentence twice
- Microphone recording and playback for speaking practice
- Lesson quizzes, scores and completion progress
- Local-device progress storage
- A clearly marked advanced-course placeholder (no real payment is collected)

## Run it on your computer
1. Extract `tamil-english-master.zip`.
2. Open a terminal in the extracted folder.
3. Start a local web server:
   - If Python is installed: `python -m http.server 8000`
4. Open `http://localhost:8000` in Chrome.
5. Try Lessons, tap Listen, complete a quiz, and test microphone recording. Allow microphone access when prompted.

Opening `index.html` directly works for lessons and browser audio, but microphone recording and install/offline features need localhost or HTTPS.

## Use on a phone
- Put the folder on an HTTPS host (for example, a static website host).
- Open the hosted URL in Chrome on Android.
- Use Chrome menu → **Install app** or **Add to Home screen**.
- Microphone recording requires HTTPS and permission.

## Build an Android APK with Capacitor (developer setup)
Prerequisites: Node.js LTS, Android Studio, and Android SDK.

1. Create a new folder and copy `index.html`, `manifest.webmanifest`, `sw.js`, and `icon.svg` into a `www` folder:
   ```
   mkdir tamil-english-android
   cd tamil-english-android
   mkdir www
   ```
2. Copy the four files into `www/`.
3. Initialize Capacitor:
   ```
   npm init -y
   npm install @capacitor/core @capacitor/cli
   npx cap init "Tamil English Master" "com.tamilenglishmaster.app" --web-dir=www
   npm install @capacitor/android
   npx cap add android
   npx cap sync android
   npx cap open android
   ```
4. In Android Studio, wait for Gradle sync. Connect an Android phone or select an emulator.
5. Press Run to test. For an APK, use **Build → Build Bundle(s) / APK(s) → Build APK(s)**.
6. Test microphone permission and audio on a real phone. For store release, create a signed Android App Bundle and follow Google Play policies.

Note: Capacitor's local app origin may handle browser APIs differently on different Android versions. Test the recording feature on the target device and configure Android microphone permission if required. For a production release, review platform permissions and privacy disclosures.

## Important limitations of this prototype
- Audio uses the speech voices installed in the user's browser/device; voice and accent vary.
- Speaking practice records the user's voice and plays it back. It does not automatically grade pronunciation yet.
- Progress is stored in that browser/device only; it does not sync across devices.
- The advanced-course button is a demo placeholder. No payment provider, account system, course access control, or real checkout is connected.
- Before charging users, add secure authentication, server-side entitlement checks, a payment provider available in your target countries, privacy policy, terms, and support contact.
