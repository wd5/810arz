# -*- coding: utf-8 -*-
DATABASE_NAME = u'810arz'
PROJECT_NAME = u'810arz'
SITE_NAME = u'ОАО 810 Авиационный ремонтный завод'
DEFAULT_FROM_EMAIL = u'support@810arz.octweb.ru'

from config.base import *

try:
    from config.development import *
except ImportError:
    from config.production import *

TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'apps.siteblocks',
    'apps.pages',
    'apps.slider',
    'apps.newsboard',
    'apps.mainblock',
    'apps.utils.items_loader',



    'sorl.thumbnail',
    #'south',
    #'captcha',
)

MIDDLEWARE_CLASSES += (
    'apps.pages.middleware.PageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'apps.pages.context_processors.meta',
    'apps.siteblocks.context_processors.settings',
)