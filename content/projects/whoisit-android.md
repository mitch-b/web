Title: Who Is It - Android
Date: 2013-12-13 18:14
Modified: 2014-01-02 23:05
Tags: android,mobile,java
Slug: whoisit-android
Summary: Android app to modify ringtone based on phone number matches

* [Source Code](https://github.com/mitch-b/whoisit-android){:target="_blank"}
* [Wiki](https://github.com/mitch-b/whoisit-android){:target="_blank"}

[![Get it on Google Play]({filename}/images/en_generic_rgb_wo_60.png)](https://play.google.com/store/apps/details?id=com.mitchbarry.android.whoisit){:target="_blank"}

At work, I support many different applications, many of which, require uptime outside of 8-5 regular workday hours. To ensure their resources could be reachable to fix any unexpected problems off-hours, my employer (as is common) provided cell phones to all its employees. Recently, the decision was made to no longer provide company cell phones, but to instead provide a monthly stipend for employees to help pay for their personal plans.

When I get a phone call from work to my personal cell phone, I'd prefer to know who is calling me based on a special vibrate pattern or ringtone when my device is not with me. If it is 2AM and I get a call from Joe Schmoe, I'd rather let it ring. If I am on-call, I know I need to take the call. The trick was that I could get a call from any number matching 402-555-*, since any employee had some variation of this pattern. Setting a regular ringtone wasn't going to cut it.

Who Is It for Android solves this problem by allowing you to enter a pattern match for incoming phone numbers. If the pattern matches an incoming caller, the phone will mute the ringer, play the custom ringtone via the Alarm audio stream, and reset audio mix when complete.

I had some struggles changing the ringtone "on-the-fly", since the phone starts ringing when a call comes in. The inner workings of this application are well explained in the [GitHub wiki](https://github.com/mitch-b/whoisit-android/wiki){:target="_blank"} articles.
