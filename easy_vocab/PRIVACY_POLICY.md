# Privacy Policy for EasyVocab (수능 영단어)

**Last Updated:** September 4, 2026

## Introduction

EasyVocab ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our mobile application EasyVocab (수능 영단어) (the "App").

Please read this privacy policy carefully. If you do not agree with the terms of this privacy policy, please do not access the application.

## Information We Collect

### 1. Automatically Collected Information

When you use the App, we automatically collect certain information about your device and usage patterns:

#### Analytics Data (via Firebase Analytics)
- Device information (model, operating system version, an app-scoped Firebase installation identifier)
- App usage data (screens viewed, features used, session duration)
- Language preferences
- Premium status (whether the one-time premium purchase has been made)
- Actions performed within the app (e.g., viewing word groups, marking words as learned, playing audio)
- Approximate location at country/region level, which Google derives from a masked IP address (Google: Analytics "derives general location data from users' masked IP addresses"). This applies to **all** users, premium included, and does not use your device's location services — the App requests no location permission
- Firebase Analytics does **not** collect your device's advertising identifier: Android Advertising ID collection is disabled in the app, and on iOS the advertising identifier is only available to Google services if you allow tracking in the system prompt. Analytics also starts with all advertising-related consent types denied and only receives your ad consent choice after you make it (see "Your Ad Consent Choices" below)

#### Crash and Performance Data (via Firebase Crashlytics)
- Crash logs and stack traces
- Device state information at the time of crashes
- App performance metrics
- Custom logs related to app errors

#### Advertising Data (via Google AdMob) — free version only
- Device advertising ID (on iOS only if you allow tracking in the system App Tracking Transparency prompt; on Android subject to your device's ad settings)
- IP address, which Google may use to estimate your approximate (city-level) location for ad delivery. Like Analytics above, this is IP-based only; the App itself requests **no** location permission and never accesses your device's location services
- Device information
- Ad interaction data (ads shown, taps)
- On iOS, ad-driven app installs may be attributed through Apple's privacy-preserving SKAdNetwork framework, which does not identify you

Advertising data is collected only while ads are shown, i.e. never for premium users, and on the first screen that shows an ad — not at app launch.

### 2. Information You Provide

#### Learning Progress Data
- Words you mark as "learned" or "familiar"
- Your progress through vocabulary levels
- Custom study preferences

#### Purchase Information (via In-App Purchases)
- Purchase transaction data for the single one-time, non-consumable premium purchase (processed by Apple App Store or Google Play Store). The App sells no subscriptions and makes no recurring charges
- Premium status (whether the one-time premium purchase has been made)
- We do not collect or store your payment information directly

## How We Use Your Information

We use the information we collect to:

1. **Provide and Maintain the App**
   - Track your learning progress
   - Save your vocabulary study history
   - Synchronize your preferences across app sessions

2. **Improve the App**
   - Analyze usage patterns to improve features
   - Identify and fix bugs and crashes
   - Optimize app performance

3. **Personalize Your Experience**
   - Display relevant vocabulary content
   - Remember your language preferences
   - Track your learning statistics

4. **Display Advertisements** (for non-premium users)
   - Show ads via Google AdMob — personalized only where you have consented (see "Your Ad Consent Choices"); otherwise non-personalized
   - Measure ad performance

5. **Process Purchases**
   - Unlock premium after the one-time purchase
   - Restore a previous purchase on a new device or after reinstalling

## Third-Party Services

We use the following third-party services that may collect information:

### Google AdMob (including Google User Messaging Platform)
- **Purpose:** Display advertisements in the free version of the app and manage advertising consent
- **Data Collected:** Device identifiers, ad interaction data, IP address (approximate location inferred by Google); your consent choices are stored on your device
- **Consent:** Google User Messaging Platform (UMP) consent form in the EEA, UK and Switzerland — a Google-certified consent management platform integrated with the IAB Transparency and Consent Framework (TCF); iOS App Tracking Transparency prompt
- **Privacy Policy:** https://policies.google.com/privacy
- **How Google uses data from partner apps:** https://policies.google.com/technologies/partner-sites

### Firebase Analytics
- **Purpose:** Understand app usage and improve user experience
- **Data Collected:** Device information, usage patterns, user actions, approximate location derived from a masked IP address (all users)
- **Privacy Policy:** https://firebase.google.com/support/privacy

### Firebase Crashlytics
- **Purpose:** Monitor app stability and fix crashes
- **Data Collected:** Crash reports, device state, stack traces
- **Privacy Policy:** https://firebase.google.com/support/privacy

### Apple App Store / Google Play Store
- **Purpose:** Process in-app purchases
- **Data Collected:** Purchase transaction data
- **Privacy Policies:**
  - Apple: https://www.apple.com/legal/privacy/
  - Google: https://policies.google.com/privacy

## Notifications and Reminders

If you turn on the daily study reminder, the App schedules **one local notification per day** at the time you choose, using the operating system's local notification service. There is no push-notification server: the reminder is created and delivered entirely on your device, and no device token or other data is sent to us or to anyone else. The notification text is a fixed message in your chosen UI language (for example "Time to Study!"); it never contains your learning data. On iOS it sets the app icon badge to 1 until you open the App.

- Reminder settings (on/off and time) are stored only on your device
- Notification permission (and, on Android 12+, the exact-alarm permission) is requested **only when you turn reminders on** — via the Settings toggle or the one-time reminder suggestion shown after you learn your first five words — never at app launch. If you never enable reminders, no permission is requested
- You can turn reminders off at any time in the App's Settings or in your device's notification settings

## Data Storage and Security

### Local Storage
- Your learning progress (words marked as learned, review schedule, study streaks, starred words) is stored locally on your device using an SQLite database
- Language, theme, reminder and daily-goal preferences are stored locally using SharedPreferences
- This data is not transmitted to our servers. We operate no server of our own
- **Backup files:** if you use "Export Progress", the App writes your learning progress to a file and hands it to the system share sheet; where it goes from there (email, cloud drive, another device) is entirely your choice. "Import Progress" reads such a file back. The backup contains only your learning progress — no identifiers

### Cloud Storage
- Analytics data is transmitted to Firebase servers
- Crash reports are transmitted to Firebase Crashlytics
- All data transmission is encrypted using industry-standard HTTPS/TLS protocols

### Data Security
We implement appropriate technical and organizational security measures to protect your information against unauthorized access, alteration, disclosure, or destruction.

## Data Retention

- **Learning Progress:** Stored locally on your device until you delete the app
- **Analytics Data:** Retained by Firebase according to its data retention settings (at most 14 months), then deleted automatically
- **Crash Reports:** Retained by Firebase Crashlytics for 90 days, then deleted automatically
- **Ad Data:** Retained by Google AdMob according to Google's policies

**Important limitation:** analytics, crash and advertising data is transmitted directly from your device to Google (Firebase, AdMob) and held on Google's systems. The App has no user accounts and we hold no name, e-mail or other identifier that would let us find the records belonging to a particular person. **We are therefore not able to locate or delete individual analytics or crash records on request.** This data is not linked to your identity, and it expires automatically under the retention periods above. Uninstalling the App stops all further collection immediately.

## Your Privacy Rights

Depending on your location, you may have the following rights:

### General Rights
- **Access:** Ask us what categories of data the App collects (this policy is the complete answer; we cannot produce a per-person extract because we cannot identify your records — see "Data Retention")
- **Deletion:**
  - **Data on your device** (learning progress, settings): delete it by uninstalling the App, or reset it by importing an empty backup
  - **Analytics and crash data at Google:** we cannot delete this individually (see "Data Retention"); it is not linked to your identity and is deleted automatically when its retention period ends
  - **Advertising data at Google:** manage or delete it through Google's own controls — your Google account's My Ad Center / Google privacy settings, your device's advertising-ID reset or deletion, and the in-app "Ad Privacy Settings" described below
- **Opt-Out of Personalized Ads:**
  - **In the App (EEA, UK, Switzerland):** Settings > Privacy > "Ad Privacy Settings" reopens the consent form so you can change or withdraw your choices at any time
  - **iOS:** Settings > Privacy & Security > Tracking > turn off "Allow Apps to Request to Track" (or deny the App's tracking prompt)
  - **Android:** Settings > Google > Ads > Delete advertising ID / opt out of ads personalization
  - **Any region:** purchasing Premium removes ads and, with them, all AdMob data collection

## Your Ad Consent Choices

- **European Economic Area, United Kingdom and Switzerland:** before the first ad is requested, the App shows Google's consent form (Google User Messaging Platform). You can accept, decline, or manage purposes and vendors individually. Ads are only requested if the form's outcome allows it; if you decline personalized advertising, Google serves non-personalized ads. You can change your decision at any time via Settings > Privacy > "Ad Privacy Settings" in the App, which is shown whenever your region requires it
- **iOS (all regions):** before the first ad is requested, iOS shows the App Tracking Transparency prompt. If you choose "Ask App Not to Track", the App does not share your advertising identifier with Google and ads are not personalized across apps
- **Firebase Analytics consent mode:** Analytics starts with the advertising-related consent types (`ad_storage`, `ad_user_data`, `ad_personalization_signals`) denied and is only told "granted" outside the regions where consent is required. Usage analytics itself (which screens you use, without an advertising identifier) is not consent-gated; see "Firebase Analytics" under "Specific Feature Data Collection"
- **Timing:** neither prompt is shown at app launch. Both appear when you first open a screen that shows ads. Premium users never see them

### GDPR Rights (EEA, UK, and Switzerland)
If you are in the European Economic Area, the United Kingdom, or Switzerland, you have additional rights under the GDPR, the UK GDPR, and the Swiss Federal Act on Data Protection:
- Right to access your personal data
- Right to rectification of inaccurate data
- Right to erasure ("right to be forgotten")
- Right to restrict processing
- Right to data portability
- Right to object to processing
- Right to withdraw consent at any time (for advertising, via Settings > Privacy > "Ad Privacy Settings" in the App)

**How these rights apply to this App:** we process no data that we can attribute to you (no account, no contact details). For the analytics and crash data described above we are unable to identify the data subject, so access, rectification, erasure and portability requests cannot be fulfilled for that data (GDPR Article 11). You can still: withdraw ad consent at any time via Settings > Privacy > "Ad Privacy Settings"; object to further processing by uninstalling the App, which ends all collection; and exercise your rights against Google for advertising data through Google's privacy controls (https://myadcenter.google.com, https://myaccount.google.com). Learning data stays on your device and is fully under your control (export, import, delete by uninstalling).

### CCPA/CPRA Rights (California Users)
If you are a California resident, you have the right to:
- Know what personal information is collected
- Know whether personal information is sold or shared
- Opt-out of the sale or sharing of personal information
- Access your personal information
- Request deletion of personal information
- Non-discrimination for exercising your rights

**Note:** We do not sell your personal information. To the extent that providing the advertising identifier to our advertising partner (Google AdMob) for personalized ads is considered "sharing" for cross-context behavioral advertising, you can opt out at any time: deny the iOS tracking prompt or turn off tracking in iOS Settings, reset or delete your advertising ID in Android Settings, use the in-app "Ad Privacy Settings" where it is shown, or purchase Premium, which removes ads and all AdMob data collection. Access and deletion requests are subject to the same limitation described under "Data Retention": we hold no identifier that would let us find your records, so we can confirm what categories are collected but cannot produce or delete a per-person record.

## Children's Privacy

Our App is not directed to children under the age of 13 (or 16 in the EEA). We do not knowingly collect personal information from children. The App never asks for a name, e-mail address or any other personal detail. If you are a parent or guardian and are concerned about your child's use of the App, uninstall it to stop all data collection; because the analytics and crash data we receive is not linked to any identity, there is no record we could look up or delete individually (see "Data Retention"). You are welcome to contact us with any questions.

## Premium Purchase

Premium is a **one-time, non-consumable in-app purchase** — there is no subscription, no trial and no recurring charge. When you buy it:
- Ads are removed from the app
- Additional features are unlocked (example audio, word management and starring for all groups)
- Your premium status is stored locally and verified through App Store/Play Store; if the store cannot confirm the purchase (for example offline), premium is kept for a 7-day grace period before it is revoked
- "Restore Purchases" in Settings re-checks the store so a purchase made on another device or before a reinstall is recognised
- We do not collect or store your payment information

## International Data Transfers

Your information may be transferred to and processed in countries other than your country of residence. These countries may have data protection laws that are different from the laws of your country.

We ensure appropriate safeguards are in place to protect your information in accordance with this Privacy Policy.

## Changes to This Privacy Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by:
- Updating the "Last Updated" date at the top of this policy
- Displaying a notice in the app (for material changes)

You are advised to review this Privacy Policy periodically for any changes.

## Contact Us

If you have questions or concerns about this Privacy Policy or our data practices, please contact us:

**Email:** hello.prseo7@gmail.com
**App:** EasyVocab (수능 영단어)
**Developer:** PrSeo7

## Consent

By using our App, you consent to our Privacy Policy and agree to its terms.

## Data Collection Summary for App Store/Play Store

### Data Used to Track You (free version, only with tracking permission)
- **Identifiers:** Advertising ID (for personalized ads)
- **Usage Data:** Advertising data
- **Location:** Coarse location inferred from IP address by Google AdMob

### Data Linked to You
- **Usage Data:** App interactions, word progress (stored locally)
- **Identifiers:** Device ID (for analytics)
- **Purchases:** In-app purchase history

### Data Not Linked to You
- **Diagnostics:** Crash logs, performance data
- **Usage Data:** Anonymous analytics
- **Location:** Coarse (country/region) location derived by Firebase Analytics from a masked IP address — all users, not used for tracking

## Specific Feature Data Collection

### AdMob (Non-Premium Users Only)
- **Collects:** Device identifiers (subject to consent/ATT), ad interaction data, IP address (approximate location inferred by Google)
- **Purpose:** Display ads; personalized only with consent
- **Opt-out:** Purchase premium, use the in-app "Ad Privacy Settings" (EEA/UK/CH), deny the iOS tracking prompt, or use device ad settings

### Firebase Analytics
- **Collects:** App usage events, screen views, user actions, keyed by an app-scoped Firebase installation ID (not your advertising ID); approximate country/region location derived from a masked IP address (all users)
- **Purpose:** Improve app performance and user experience
- **Opt-out:** Usage analytics cannot be switched off inside the App, but it contains no advertising identifier and the advertising-related consent types are denied by default. Uninstalling the App stops all collection; records already received cannot be deleted individually by us and expire automatically (see "Data Retention")

### Firebase Crashlytics
- **Collects:** Crash reports, device state, app logs
- **Purpose:** Fix bugs and improve app stability
- **Opt-out:** Data collection is automatic for app stability

### In-App Purchases
- **Collects:** Purchase transaction data (via App Store/Play Store)
- **Purpose:** Manage premium features
- **Storage:** Verified through platform receipts

### Notifications
- **Collects:** Nothing — reminder time and on/off state are stored only on your device; local notifications only, no push service or device tokens
- **Purpose:** Optional daily study reminder
- **Opt-out:** Turn reminders off in the App's Settings or in your device's notification settings; permission is only ever requested when you turn them on

## Your Choices

1. **Ad Consent:** Change your choices in-app via Settings > Privacy > "Ad Privacy Settings" (EEA/UK/CH), or deny the iOS tracking prompt
2. **Limit Ad Tracking:** Use iOS/Android settings to opt-out of personalized ads
3. **Delete Data:** Uninstall the app to remove all locally stored data and stop all collection. Analytics and crash data already sent to Google cannot be deleted by us individually and expires automatically
4. **Premium Purchase:** Buy the one-time premium upgrade to remove ads and all advertising data collection
5. **Reminders:** Turn the daily reminder on or off in Settings; no permission is requested unless you turn it on
6. **Contact Us:** Ask us anything about this policy or our data practices

## Change History

- **September 4, 2026:** Added the in-app GDPR consent form (Google UMP) and the Settings > Privacy > "Ad Privacy Settings" entry; described the iOS App Tracking Transparency prompt and its timing (first ad screen, not launch); stated that Firebase Analytics does not collect the advertising ID and starts with ad consent denied; clarified that "location" means Google's IP-based approximate location inference and that the App requests no location permission; described backup files; added SKAdNetwork. Same day: corrected the deletion and access wording — analytics and crash data goes straight to Google, is not linked to any identity and cannot be located or deleted by us individually; it expires automatically. Earlier versions implied we could delete it on request. Also corrected: approximate (country/region) location is derived from the IP address not only by AdMob for free users but also by Firebase Analytics for **all** users; an earlier wording implied only the free version involved location. Also corrected: premium is a one-time, non-consumable purchase, not a subscription — earlier wording said "premium subscription". Re-merged the sections that the published July 26, 2026 revision already had and this rewrite had dropped: "Notifications and Reminders" (plus the Notifications feature entry), "CCPA/CPRA Rights" with the sharing opt-out, the EEA/UK/Switzerland scope of the GDPR section, and UMP described as a TCF-integrated consent platform
- **July 26, 2026:** Published revision: advertising consent (UMP/ATT), reminders, one-time premium purchase
- **December 30, 2024:** First version

---

**This privacy policy is effective as of September 4, 2026.**
