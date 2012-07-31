# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from apps.siteblocks.models import Settings
from apps.slider.models import Photo

class ShowContactsView(TemplateView):
    template_name = 'siteblocks/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ShowContactsView, self).get_context_data(**kwargs)

        try:
            context['phone'] = Settings.objects.get(name='phonenum').value
        except:
            context['phone'] = ''
        try:
            context['address'] = Settings.objects.get(name='address').value
        except:
            context['address'] = ''
        try:
            context['contact_map'] = Settings.objects.get(name='contact_map_coord').value
        except:
            context['contact_map'] = False

        return context

show_contacts = ShowContactsView.as_view()

