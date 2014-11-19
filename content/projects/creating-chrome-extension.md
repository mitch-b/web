Title: SAP Note Chrome Extension
Date: 2014-11-18 22:53
Modified: 2014-11-18 22:53
Tags: js,chrome,sap
Slug: sap-note-chrome-extension
Summary: While at work, I thought of a quick way to speed up some of the waiting time that both developers and our process teams deal with every day. I finally had a "good" reason to try my hand at a Chrome Extension...
About_author: tries to improve productivity

* [Source Code](https://github.com/mitch-b/sap-note-chrome-extension)
* [SAP Support Note QuickLaunch](https://chrome.google.com/webstore/detail/sap-support-note-quicklau/coihbaakfmcepaofjibgkalgpjpbjnnm)

After recently receiving my S-User login credentials from work to start poking around SAP's knowledgebase, I discovered the pain that is searching for SAP Notes. I did notice that linking to a note had an easy to read URL, with the note number simply appended at the end.

Great, I can build a box, you can enter in the note number, and I can open a new tab directly to that note. Easy, and saves about a minute of time. That's all well and good, but what benefit is that over copying a template URL, pasting that into the browser and then just appending the note number? Not a whole lot.

Another frequent activity is searching for notes which may exist to resolve an existing problem in the system. As it turns out, this is another functionality we can utilize URL parameters for. This is shaping up to be enough to start taking action! Since an API is not provided, and I'm looking for a quick solution anyway, this is great.

So, I build a single HTML page with a text box and a button. You can enter a number (signifying a note), or an alpha-numeric value (signifying searching for a note). The two are distinct rules which are also easy to check (`isNaN()`). The hardest part was finding out how to lay out the project structure and the `manifest.json` components -- which really ended up not being difficult at all.

All things considered, concept, build and deployment took about an hour. After I finished and got the extension out on the Web Store, I noticed existing extensions which already offered this functionality (and more). They're mostly all the same, but I'm glad I took the time to build my own, if not to help demystify Chrome Extensions.

If you're looking to start your own extension, take a look at the source, it will help point you in the right direction.
