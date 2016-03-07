#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'N'
SITENAME = u'Microbial Musings'
SITEURL = 'http://kove.pw/mm'
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

THEME = 'kove-theme'

# Uncomment following line if you want document-relative URLs when developing.
# When Testing a theme, you will need to uncomment this, then comment before git push
# RELATIVE_URLS = True

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Twitter', 'http://twitter.com/welcomeback_rr'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

#some throw ins
#if not specified generate URL slug based on title, not filename or anything else
SLUGIFY_SOURCE = 'title'

#I've always hated Cache for these types of projects
LOAD_CONTENT_CACHE = False
