#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

THEME = "../" + os.environ.get("PELICAN_THEME", "the-plain")

AUTHOR = 'Julien Hadley Jack'
SITENAME = "Theme Demo"
SITEURL = ''
SITESUBTITLE = "This is some sample text to be shown. It is a bit longer to showcase line breaks."

TIMEZONE = "Europe/Paris"

REVERSE_CATEGORY_ORDER = True
DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 4

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Biologeek', 'http://biologeek.org'),
         ('Filyb', "http://filyb.info/"),
         ('Libert-fr', "http://www.libert-fr.com"),
         ('N1k0', "http://prendreuncafe.com/blog/"),
         ('Tarek Ziadé', "http://ziade.org/blog"),
         ('Zubin Mithra', "http://zubin71.wordpress.com/"),)

# Social widget
SOCIAL = (
  ('github', 'https://github.com/julien-hadleyjack'),
  ('facebook', 'https://www.facebook.com/julien.hadleyjack'),
  ('google', 'https://plus.google.com/+JulienHadleyJack/'),
  ('linkedin', 'https://de.linkedin.com/pub/julien-hadley-jack/82/ba9/705'),
  ('xing', 'https://www.xing.com/profile/Julien_HadleyJack'),
  ('twitter', 'http://twitter.com/ametaireau'),
  ('lastfm', 'http://lastfm.com/user/akounet'),
  ('github', 'http://github.com/ametaireau')
)

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    ]



TAG_DESCRIPTION = {"python": "This is test description for the python tag."}

SHARE = True

# DISQUS_SITENAME = "hadleyjack-de"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
