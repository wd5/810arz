# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('apps.newsboard.views',
    url(r'^/$', 'news_list', name='news_list', ),
    url(r'^/view/(?P<pk>\d*)/$', 'news_detail', name='news_detail'),

)
