#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

THEME = "../" + os.environ.get("PELICAN_THEME", "the-plain")

AUTHOR = 'Alexis Métaireau'
SITENAME = "Alexis' log"
SITEURL = 'http://blog.notmyidea.org'
SITESUBTITLE = "This is some sample text to be shown. It is a bit longer to showcase line breaks."


TIMEZONE = "Europe/Paris"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/ametaireau/'
DISQUS_SITENAME = "blog-notmyidea"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

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

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    ]

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"




TAG_DESCRIPTION = {"python": "This is test description"}

SHARE = True

# DISQUS_SITENAME = "hadleyjack-de"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
