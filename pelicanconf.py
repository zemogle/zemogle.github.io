AUTHOR = 'Edward Gomez'
SITENAME = 'Edward Gomez'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/bulma_profile/'

# Blogroll
LINKS = (('About', '/about/'),
         ('CV', '/curriculum-vitae/'),
         ('Talks', '/talks/'),
         ('Videos', '/videos/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LANDING_PAGE_TITLE = "Edward's Profile"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
