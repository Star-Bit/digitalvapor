#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'StarBit and DigitalVapor'
AUTHOR_EMAIL = u'contact@antivapor.net'
AUTHOR_GPLUS = '106765113086639417627' #Your Google Plus profile ID, see https://support.google.com/webmasters/answer/2539557?hl=en
SITENAME = u'Digital Vapor'
SITEURL = 'http://antivapor.net'
HEADERTITLE = u'Digital Vapor and Star Bits'
DESCRIPTION = u'We sell terrariums, gadgets, and art.'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = None
FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('DigitalVapor on iNaturalist', 'http://inaturalist.org/observations/digitalvapor'),
		      ('StarBit on iNaturalist', 'http://inaturalist.org/observations/star_bit'),
			('Fork The Cookbook','http://forkthecookbook.com/antivapor'))

# Social widget, use font-awesome name for first item in tuple
SOCIAL = (('github-alt', 'https://github.com/digitalvapor'),
		      #('google-plus','#google-plus'),
          ('twitter', 'http://twitter.com/antivapor'),
          ('rss',SITEURL+'/feeds/all.atom.xml'),
          #('facebook','#facebook'),
          #('cloud','#soundcloud'),
          #('flickr','#flickr'),
          #('pagelines','#inaturalist'),
          #('globe','#inaturalist'),
          #('vimeo-square','https://vimeo.com/digitalvapor'),
          ('youtube-play','https://youtube.com/user/fondasaurusrex'),)

MENUITEMS = (#('About Us','pages/about.html'),
			       #('Contact','pages/contact.html'),
			       ('Products','https://starvapor.etsy.com'),)

DEFAULT_PAGINATION = 10
#SUMMARY_MAX_LENGTH = None
#-----------
# PATH RELATED
#-----------
RELATIVE_URLS = True
IMAGE_PATH = 'images' #used by Thumbnailer
THUMBNAIL_DIR = IMAGE_PATH #used by Thumbnailer, I just want it all in images
#CODE_DIR = 'code' #used by liquid_tags.include_code
STATIC_PATHS = [IMAGE_PATH,'audio','extra/robots.txt','cv/spalding_resume.pdf']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
'cv/spalding_resume.pdf': {'path': 'spalding_resume.pdf'},}
PATH = 'content'
OUTPUT_PATH = 'output'
#-----------
# Deploy Related
#-----------
IGNORE_FILES = (['themes/icosahedron/static/css/sass/*'])
OUTPUT_RETENTION = ('.git')
#-----------
# THEME RELATED
#-----------
THEME = 'themes/icosahedron'
SYMBOL = u'mandala.png'
ABOUTUS_INTRO = "We like space and nature, gadgets and cats, coffee and jasmine lattes. We're bad at skateboarding, but good at drawing skateboarders being eaten by a gigantic arthropod, who weaves vortex cocoons and poops beautiful crystals."
ABOUTUS_BODY = "We're currently starting small with the \"business\" and we take lots of comic book and coffee breaks, sorry. We propogate carnivorous plants, and succulents, and sell terrariums. [<a href='star-bit'>Star-Bit</a>] is great at printmaking and drawing yetis, and [<a href='digitalvapor'>digitalvapor</a>] likes to draw hairy things with lots of dots. [<a href='digitalvapor'>digitalvapor</a>] is also working on some gadgets that will be pretty dope, but they're still in the development phase. Thanks for taking a look!"
BITCOIN = '15g4JLeCc5xW7sq3W3VjYNENXD7sAUzZ46'
DOGECOIN = 'DJWZMij6LDsTXyMqzK8oKLhq2BKZAmyNjN'
LITECOIN = 'LUGzXpgKHvnPUw7BzB6xH8PHF8PA9LfzEX'
# TODO: If Fontawesome gets Litecoin and Dogecoin icons, I'll update this to include those fonts.
DONATE = (('฿',BITCOIN),
          ('Ł',LITECOIN),
          ('Ð',DOGECOIN),)
LIVERELOAD = True
ADDRESS = (    ('name',SITENAME),
               ('streetAddress','Farallon Islands'),
               ('addressLocality','San Francisco'),
               ('addressRegion','CA'),
               # ('postalCode',''),
               # ('addressCountry',''),
          )
#-----------
# PLUGIN RELATED
#-----------
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['share_post','gravatar','grid','sitemap','liquid_tags.img','liquid_tags.gram']#'optimize_images''thumbnailer',,'gzip_cache','minify',, 'liquid_tags.video','liquid_tags.youtube', 'liquid_tags.vimeo','liquid_tags.include_code', 'liquid_tags.notebook'
DISQUS_SITENAME = "digitalvapor"
GOOGLE_ANALYTICS = "UA-44642246-3"
ETSY_API_KEY = '8z7rq5zh48tkg3mv4be7avle'
ETSY_SHOPNAME = 'starvapor'
ETSY_STORE = 9420461
USE_BUTTON = True
COOK = 'antivapor'
SITEMAP = {
    'format': 'xml',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 0.5
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly'
#     }
}
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
THUMBNAIL_SIZES = {
#	'thumb_square': '150',
	'thumb': '150x?',
#     'thumb_tall': '?x150',
#	'mid': '500x?',
#	'big': '1000x?',
	'max': '2000x?',
}
#THUMBNAIL_KEEP_NAME = False
