# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url

from views import index
from pages.views import show_about
from apps.siteblocks.views import show_contacts
from apps.mainblock.views import show_licenses, show_structure, purchases_list, items_loader_by_ids
from apps.newsboard.views import news_list, news_detail
from apps.utils.items_loader.views import items_loader
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    url(r'^$',index, name='index'),
    (r'^load_items/$',csrf_exempt(items_loader)),
    (r'^load_items_by_ids/$',csrf_exempt(items_loader_by_ids)),
    (r'^about/$',show_about),
    (r'^contacts/$',show_contacts),

    (r'^licenses/$',show_licenses),

    (r'^structure/$',show_structure),

    (r'^news/$', news_list),
    url(r'^news/(?P<pk>\d*)/$', news_detail, name='news_detail'),

    (r'^purchases/$', purchases_list, {'type':'current'}),
    (r'^purchases/(?P<type>[^/]+)/$', purchases_list),

)
#url(r'^captcha/', include('captcha.urls')),

#urlpatterns += #app_url


