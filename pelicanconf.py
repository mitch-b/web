#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mitchell Barry'
AUTHOR_EMAIL = u'mitch.barry@gmail.com'
SITENAME = u'Mitchell Barry'
SITEURL = 'http://localhost:8000'

PATH = 'content'
THEME = 'notmyidea'
THEME = 'themes/pure'


TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravitar','sitemap','tipue_search',]

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('google-plus', 'https://google.com/+MitchellBarry'),
          ('github', 'https://github.com/mitch-b'),
          ('twitter','https://twitter.com/mitchbarry'),)

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
	('Archive', 'archives.html'),
	('About', 'about/'),
	('Projects', 'category/projects.html'), ]

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
# ARTICLE_EXCLUDES = [('projects'),]

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# These folders will copy from content to output directly
STATIC_PATHS = ['images', 'assets', ]

# Pure theme settings
COVER_IMG_URL = '/images/zealandia.jpg'
PROFILE_IMAGE_URL = '/images/glass.jpg'
TAGLINE = 'Software Developer, Person'
DISQUS_SITENAME = ''
GOOGLE_ANALYTICS = ''

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
