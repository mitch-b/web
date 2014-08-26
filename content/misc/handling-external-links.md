Title: Handling External Links
Date: 2014-08-26 15:09
Modified: 2014-08-26 15:09
Tags: blog,web
Slug: handling-external-links
Summary: How to handle user experience on your site with external links
About_author: muses about UX

As I'm reading any given blog, I'm never sure how external links are handled.  External link? What are you talking about? These are links which point to a third-party domain from where you are. For example, you're currently on the `mitchbarry.com` domain -- but if I link to Google, that's taking you away from your current context.

It's my job as the author of the post to make sure you understand where a link is taking you. I might want to extend a current thought by linking to a previous post, so I'll link over to that article within the current domain. The style of the page I'm linking to *should* be inherently familiar to you, so the switch is not jarring.

A link outside of my domain will, conversely, have a different feel. To prepare for that, I'll add a small indicator to let you know it's external. On top of that, right now I have it defaulting to open all external links in a new tab/window. I'm still on the fence whether or not I will keep this functionality, but it does fit in line with my expectation that the reader shouldn't lose context with the current article. Instead, I'll open my linked content without forcing you to lose your place.

Pelican doesn't have a setting to automatically set this feature. Since I use the Markdown format for all of my posts, I was using a special markup to generate proper HTML to open links in a new tab/window. So I had the following structure put in every external link:

    :::Markdown
    Follow this [link](https://google.com/){:target="_blank"}

This works fine until one day when I forget to add it! I toyed with the option of creating a Pelican plugin to modify my links at site generation time - and that might be a better long term goal.

In the interim, I've created a quick JavaScript [solution](https://github.com/mitch-b/web/blob/master/content/assets/auto-target.js):

    :::javascript
    (function() {
        var hostname = window.location.hostname;
        var new_tab = true;
        var set_icon = true;
        for (var links = document.links, i = 0, a; a = links[i]; i++) {
            if (a.hostname !== hostname) {
                if (new_tab)
                    a.target = '_blank';
                if (set_icon)
                    a.innerHTML +=
                        '<i class="fa fa-external-link fa-1 external-link-margin" />';
            }
        }
    })();

When embedded in my articles right before the `</body>` tag, it runs through all the links it can find and applies the target and/or icon to each external link. If you've used it before, you'll notice I'm using [Font Awesome](http://fortawesome.github.io/Font-Awesome/icon/external-link/) for the external link icon. (Wow, that was so meta!)
