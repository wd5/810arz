# -*- coding: utf-8 -*-
from apps.siteblocks.models import Settings
from settings import SITE_NAME

def settings(request):

    return {
        'site_name': SITE_NAME,
    }