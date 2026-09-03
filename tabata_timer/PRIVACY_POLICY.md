# Tabata Timer Privacy Policy

_Last updated: 2026-09-04_

Tabata Timer (the “App”) is provided by PrSeo7 (“we”, “us”, or “our”). We value your privacy and want you to understand how we handle your information when you use the App on iOS or Android devices. This policy describes what data we collect, how we use it, and the choices you have. The App does not require you to create an account, and we do not knowingly collect information that can directly identify you.

---

## 1. Information We Collect

### 1.1 Data you provide locally
- **Interval settings and preferences** (e.g., preparation/work/rest durations, beep toggle) are stored only on your device using the operating system’s secure storage (SharedPreferences on Android / NSUserDefaults on iOS). We cannot access this data.

### 1.2 Automatically collected diagnostic data
- **Usage analytics**: Firebase Analytics records anonymous events such as button taps, screen views, and device coarse information (model, OS version, locale) to help us understand which features are most helpful. This runs from your first launch and is not tied to the ad consent dialog described below. It is configured so that it does not collect your Advertising ID or IDFA and does not store or share data for advertising purposes; it is used only for aggregated product analytics and is separate from the advertising data in section 1.3.
- **Crash reports**: Firebase Crashlytics collects stack traces, anonymized device identifiers, OS version, and the state of the app when a crash occurs so we can fix stability issues quickly.

### 1.3 Advertising data
- The App uses **Google Mobile Ads (AdMob)** to show banner and interstitial ads after an initial ad-free period. AdMob may collect device identifiers (e.g., Advertising ID or IDFA), IP address, coarse location, language, and interaction data to deliver and measure ads. When you are in Firebase Test Lab or running a debug build, we force Google’s test ads.
- **Ad consent timing**: No ad-related data is collected during the initial ad-free period. Where required by law (for example in the EEA, the UK and Switzerland), a consent dialog is shown the first time you open the App after that period, before any ad is requested. Until you respond, no ads are shown. You can change your choice later from the privacy options entry in the App’s Settings tab.
- On iOS, the ad consent flow may present Apple’s App Tracking Transparency prompt before AdMob accesses the IDFA. The App does not read the IDFA itself. If you decline, or if the prompt is not shown, AdMob serves non‑personalized ads.

### 1.4 Device permissions
- **Tracking permission (iOS)**: May be requested as part of the ad consent flow, only to determine whether personalized ads can be shown. The App still works if you deny it.
- **Audio playback & wakelock**: Used to play countdown beeps and keep the screen awake during a workout. No audio recordings or motion data are collected.

### 1.5 Premium purchase
- The App offers a one-time **Premium** purchase (removes ads and unlocks landscape). Payment is handled entirely by Apple (App Store) or Google (Google Play). We never see your payment details; the store shares with the App only whether this product is owned.
- Your Premium status is stored on your device (SharedPreferences / NSUserDefaults) so it works offline and immediately at launch. On each launch the App re-checks ownership with the store using the store’s own client API. There is no server of ours involved and no receipt is sent to us. If the store reports that the product is not owned, or cannot be reached for an extended period, Premium is turned off until the store confirms it again. **Restore purchases** in Settings re-reads ownership from the store on a new device or after a reinstall.
- Purchase and restore actions are recorded in Firebase Analytics as anonymous events, including the price and currency of a completed purchase for revenue reporting. No payment instrument or store account identifier is included.

We do not collect contact lists, precise location, health data, or payment information.

---

## 2. How We Use Information

We use the data described above to:
1. Provide core Tabata timer functionality (store your configuration locally).
2. Improve performance, reliability, and user experience through aggregated analytics.
3. Diagnose and fix crashes or bugs.
4. Show ads that fund future development and keep the App free, and remove them for Premium purchasers.
5. Comply with legal obligations and enforce our terms.

We never sell your personal data.

---

## 3. Sharing With Third Parties

We share data only with service providers that help us operate the App:
- **Google/Firebase** (Firebase Analytics, Firebase Crashlytics, Google Mobile Ads) – analytics, crash diagnostics, and advertising.
- **Apple / Google** (App Store, Google Play) – to distribute the App, process the Premium purchase and confirm its ownership, and process crash metadata supplied by the OS.

Each provider processes data under its own terms and privacy policies. We may also disclose data if required by law, regulation, legal process, or governmental request, or to protect the rights, property, or safety of our users or the public.

---

## 4. Data Retention

- Local settings, including the stored Premium status, remain on your device until you uninstall the App or reset it from your operating system settings. Ownership itself is kept by Apple or Google under your store account and can be restored at any time.
- Analytics and crash logs are retained by Firebase for the period necessary to analyze trends (generally up to 26 months, subject to Google’s policies).
- AdMob retains advertising data according to Google’s policies.

Because analytics and crash data carry no identifier that we control, we cannot locate a specific person’s records to delete them individually. They are deleted automatically when the retention period ends.

---

## 5. Your Choices & Rights

- **Analytics**: The App has no in-app switch for Firebase Analytics, and it does not use your Advertising ID, so resetting that ID or the iOS “Share Analytics” setting does not affect it. Analytics events are not linked to your name, account or any identifier we control, so we cannot locate a specific person’s records to delete them on request. Uninstalling the App stops further collection, and Firebase deletes the data automatically at the end of its retention period (section 4).
- **Ad consent**: Where the consent dialog applies to you (see section 1.3), a **Privacy options** entry in the App’s Settings tab lets you review or change your choice at any time. New ad requests follow the changed choice; an ad already on screen may stay until the next launch. Outside those regions the entry is not shown and the platform controls below apply.
- **App Tracking Transparency**: On iOS you can deny or revoke permission at any time in Settings ▸ Privacy & Security ▸ Tracking. The App shows non‑personalized ads when tracking is not allowed.
- **Advertising controls**: Use your platform’s controls (reset the Advertising ID, opt out of ads personalization on Android; Tracking settings on iOS) to limit personalized ads. AdMob will still deliver contextual ads.
- **Remove ads**: Buying **Premium** removes ads entirely and the App stops requesting them. Analytics and crash reporting continue.
- **Reset local data**: Clear the App’s storage/cache or reinstall it to remove saved intervals, preferences and the stored Premium status. Premium can be brought back with **Restore purchases** in Settings.

Residents of the EEA, UK, California, and other regions with data-protection laws may have additional rights (access, correction, deletion, objection, portability). Contact us to exercise these rights; we may request information to verify your identity before acting on your request.

---

## 6. Children’s Privacy

Tabata Timer is designed for general fitness users and is not directed to children under 13 (or the relevant minimum age in your jurisdiction). We do not knowingly collect personal data from children. If you believe a child has provided us data, please contact us so we can delete it.

---

## 7. International Transfers

We operate from the Republic of Korea and may process data on servers located in other countries (e.g., the United States, Singapore, or EU regions operated by Google). These locations may have privacy laws different from yours. We rely on standard contractual clauses or comparable safeguards offered by our service providers to protect your information during transfers.

---

## 8. Security

We implement reasonable administrative, technical, and physical safeguards to protect the data we control. However, no method of transmission or storage is completely secure, so we cannot guarantee absolute security. Please use the App responsibly and keep your device up to date.

---

## 9. Changes to This Policy

We may update this Privacy Policy to reflect new features, legal requirements, or service providers. We will change the “Last updated” date above and may provide in-app notices for material changes. Your continued use after changes means you accept the updated policy.

---

## 10. Contact Us

If you have any questions or privacy requests, contact:

**PrSeo7**
Email: hello.prseo7@gmail.com

Please include “Tabata Timer Privacy” in the subject line and describe your request. We will respond as soon as reasonably possible.

---

Thank you for trusting Tabata Timer with your training. We remain committed to protecting your privacy while delivering a focused, reliable workout experience.
