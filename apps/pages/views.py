# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
from apps.pages.models import Page
from apps.slider.models import Photo
import settings

def index(request):
    try:
        page = Page.objects.get(url='index')
    except Page.DoesNotExist:
        page = False
    return direct_to_template(request, 'pages/index.html', locals())


def page(request, url):
    if not url.endswith('/'):
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    page = get_object_or_404(Page, url__exact=url)
    return direct_to_template(request, 'pages/default.html', locals())


@csrf_exempt
def static_page(request, template):
    return direct_to_template(request, template, locals())


class ShowAboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super(ShowAboutView, self).get_context_data(**kwargs)
        context['slider'] = Photo.objects.filter(show=True)

        try:
            context['page'] = Page.objects.get(id=1)
        except Page.DoesNotExist:
            context['page'] = False
        return context

show_about = ShowAboutView.as_view()

