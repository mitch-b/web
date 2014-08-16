Title: My Experience with Pelican
Date: 2014-08-16 14:46
Modified: 2014-08-16 14:46
Tags: pelican,python,blog
Slug: experience-with-pelican
Summary: Pelican has gotten me from 0 to what you're reading right now over the course of 2 days. How did it go?

##Finding the right tool
I was underway on the new [mitchbarry.com](http://mitchbarry.com) development using Angular, and I was quickly realizing how much work I was putting in, with what my goals were. As I saw it, I needed:

* A place to store my project work
* A place to write down my thoughts (you may call that a blog)

... and that was about it. So all the effort I was putting into styling, project layout, and worrying about what my backend was going to look like seemed like a little more effort than I was willing to put into it. I knew static site generators existed, the big player being [Jekyll](http://jekyllrb.com/) these days, but I had never taken a close look at them or considered it as a valid option. I chose [Pelican](http://getpelican.com) solely because it was the first result I found that used Python to generate the site. If I were more comfortable with Ruby, I'd consider migrating to Jekyll someday.

##Building the site

Rather than building my own CMS, or dealing with [WordPress](https://wordpress.com/) or [Drupal](https://www.drupal.org/start)'s overhead, I just wanted an easy way to manage content. Files to the rescue! As typical with the more popular static site generators, all you need to do is create a "posts" directory, declare your templates (what a footer, index, or article page looks like), and you're already 90% of the way there.

All I needed to do, was run a single command to jump-start my site!

    #!bash
    $> pelican-quickstart

After answering a few prompts, it created a nice looking structure:

    yourproject/
    ├── content
    │   └── (pages)
    ├── output
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish

You can see the structure I am using today at the Source link in the footer.

##Adding content
I was surprised to find that Pelican doesn't provide a handy way of inserting new content into your site. As a developer, of course I'm not going to simply create new files like everyone else. I'm going to write a script. Since my format of choice is Markdown, I created a simple Python script to drop a new Markdown file in the proper folder location after asking for some data which I find relevant for each blog post. You can take a look here for the latest version of my script - [`new.py`](https://raw.githubusercontent.com/mitch-b/web/master/new.py).

##Theming
This is one area where there are many pros and cons. Since I didn't want to spend too much time styling my site, I looked to the internet. Thankfully, Pelican does offer some [advertised themes](https://github.com/getpelican/pelican-themes) to choose from. I happened to really enjoy the Pure theme (see footer for details), and cloned the repo into my project. I eventually removed all the git references and started editing the files as just a subfolder of my current project. I tweaked some visuals, and modified the sidebar.

*If I could do it all again*, I'd keep my theme as a git submodule, but a forked copy of the original PureTheme repo. In this way, I could still merge any updates the original author has made, while keeping any theme edits outside of my website repo. In this way, I could keep my styling development separate from my web content.

##Deploying
I decided to not use GitHub Pages as my deployment destination, but instead use my own server. This meant that all I needed to do was drop my files on my webserver, and point [nginx](http://nginx.org/) to the right directory. Pelican does provide a nice Makefile which uses rsync to deploy all the site files if you choose. I did create an [`init_makefile.py`](https://raw.githubusercontent.com/mitch-b/web/master/init_makefile.py) script for anyone who wants to clone my site. By running the script, you can enter your own SSH values so you don't need to mess with editing the file or forgetting to do so.

##Maintaining
Maintenance is a breeze. Since the site is all static HTML (with a little JavaScript for search), the load on my webserver is minimal. Adding new content (including this article) was a simple as running my Python script, then adding in my Markdown to add text!

##Closing

Would I do it again with a static site generation tool? Definitely. At this time, I'm not sure what I'd want loaded into any of my pages dynamically. At some point I need to find a way to integrate my [Commit Aggregator]({filename}/projects/commit-aggregator.md), but that's for another day.

Would I try Jekyll? Certainly. If I was a bit more familiar with Ruby I would've gone that route. There's still potential in the future to look into that avenue - although I'd need to revisit theming!