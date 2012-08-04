# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from apps.siteblocks.models import Settings
from apps.mainblock.models import Purchase



class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        try:
            context['phone'] = Settings.objects.get(name='phonenum').value
        except:
            context['phone'] = ''
        context['purchases'] = Purchase.objects.published()[:3]
        return context

index = IndexView.as_view()