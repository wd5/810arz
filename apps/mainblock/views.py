# -*- coding: utf-8 -*-
from django.db.models.loading import get_model
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import TemplateView, ListView, View
from apps.mainblock.models import License, Person, Purchase, Document
from apps.siteblocks.views import Settings
from apps.slider.models import Photo
from pytils.translit import translify
import os, settings

class ShowLicensesView(ListView):
    model = License
    context_object_name = 'licenses'
    template_name = 'mainblock/licenses_list.html'
    queryset = License.objects.published()

show_licenses = ShowLicensesView.as_view()

class ShowDocumentsView(ListView):
    model = Document
    context_object_name = 'documents'
    template_name = 'mainblock/documents_list.html'
    queryset = Document.objects.published()

    def get_context_data(self, **kwargs):
        context = super(ShowDocumentsView, self).get_context_data(**kwargs)

        try:
            loaded_count = int(Settings.objects.get(name='loaded_count').value)
        except:
            loaded_count = 8
        queryset = context['documents']
        result = GetLoadIds(queryset, loaded_count)

        splited_result = result.split('!')
        try:
            remaining_count = int(splited_result[0])
        except:
            remaining_count = False
        next_id_loaded_items = splited_result[1]

        context['documents'] = context['documents'][:loaded_count]
        context['next_id_loaded_items'] = next_id_loaded_items
        context['loaded_count'] = loaded_count
        return context

show_documents = ShowDocumentsView.as_view()


class ShowStructureView(ListView):
    model = Person
    context_object_name = 'pesrons'
    template_name = 'mainblock/structure_list.html'
    queryset = Person.objects.published()

show_structure = ShowStructureView.as_view()

def sizeof_fmt(num):
    for x in ['байт', 'Кб', 'Мб', 'Гб']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


def GetLoadIds(queryset, loaded_count):
    counter = 0
    next_id_loaded_items = ''
    for item in queryset[loaded_count:]:
        counter = counter + 1
        div = counter % loaded_count
        next_id_loaded_items = u'%s,%s' % (next_id_loaded_items, item.id)
        if div == 0:
            next_id_loaded_items = u'%s|' % next_id_loaded_items

    if next_id_loaded_items.startswith(',') or next_id_loaded_items.startswith('|'):
        next_id_loaded_items = next_id_loaded_items[1:]
    if next_id_loaded_items.endswith(',') or next_id_loaded_items.endswith('|'):
        next_id_loaded_items = next_id_loaded_items[:-1]
    next_id_loaded_items = next_id_loaded_items.replace('|,', '|')

    next_block_ids = next_id_loaded_items.split('|')[0]
    if next_block_ids != '':
        next_block_ids = next_block_ids.split(',')
        next_block_ids = len(next_block_ids)
        if loaded_count > next_block_ids:
            loaded_count = next_block_ids
    else:
        loaded_count = False

    result = u'%s!%s' % (loaded_count, next_id_loaded_items)
    return result


class ShowPurchasesListView(ListView):
    model = Purchase
    context_object_name = 'purchases'
    template_name = 'mainblock/purchases_list.html'
    queryset = Purchase.objects.published()

    def get_queryset(self):
        from django.db.models import Q

        query = self.queryset.published()
        curr_type = self.kwargs.get('type', None)
        query = query.filter(type=curr_type)
        return query

    def get_context_data(self, **kwargs):
        context = super(ShowPurchasesListView, self).get_context_data(**kwargs)

        purch_doc_file = False
        curr_ext = False
        size = False
        for root, dirs, files in os.walk(settings.MEDIA_ROOT + '/uploads/', ):
            for filename in files:
                name, ext = os.path.splitext(translify(u'%s' % filename).replace(' ', '_'))
                if name == 'purchase_doc':
                    purch_doc_file = '/media/uploads/' + filename
                    curr_ext = ext
                    size = os.path.getsize(settings.MEDIA_ROOT + '/uploads/' + filename)

        context['purch_doc_file'] = purch_doc_file
        if curr_ext:
            context['ext'] = curr_ext[1:]
        if size:
            size = sizeof_fmt(size)
        context['size'] = size
        context['type'] = self.kwargs.get('type', None)

        try:
            loaded_count = int(Settings.objects.get(name='loaded_count').value)
        except:
            loaded_count = 6
        queryset = context['purchases']
        result = GetLoadIds(queryset, loaded_count)

        splited_result = result.split('!')
        try:
            remaining_count = int(splited_result[0])
        except:
            remaining_count = False
        next_id_loaded_items = splited_result[1]

        context['purchases'] = context['purchases'][:loaded_count]
        context['next_id_loaded_items'] = next_id_loaded_items
        context['loaded_count'] = loaded_count
        return context

purchases_list = ShowPurchasesListView.as_view()

def isodd(num):
    return num & 1 and True or False


class ItemsByIdLoaderView(View):
    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseRedirect('/')
        else:
            if 'load_ids' not in request.POST or 'm_name' not in request.POST or 'a_name' not in request.POST:
                return HttpResponseBadRequest()

            try:
                loaded_count = int(request.POST['loaded_count'])
            except:
                loaded_count = False
            if loaded_count:
              is_odd = isodd(loaded_count)
            else:
              is_odd = False
            loaded_count = loaded_count*2

            load_ids = request.POST['load_ids']
            app_name = request.POST['a_name']
            model_name = request.POST['m_name']
            model = get_model(app_name, model_name)

            load_ids_list = load_ids.split('|')
            block_id = load_ids_list[0]
            load_ids = load_ids.replace(block_id, '')
            block_id = block_id.split(',')

            if load_ids.startswith(',') or load_ids.startswith('|'):
                load_ids = load_ids[1:]
            if load_ids.endswith(',') or load_ids.endswith('|'):
                load_ids = load_ids[:-1]

            try:
                next_ids = load_ids_list[1].split(',')
            except:
                next_ids = False

            if next_ids:
                remaining_count = len(next_ids)
            else:
                remaining_count = -1

            try:
                queryset = model.objects.published().filter(id__in=block_id)
            except model.DoesNotExist:
                return HttpResponseBadRequest()


            if model_name=="Document":
                template_name = 'items_loader/documents_load_template.html'
            else:
                template_name = 'items_loader/purchases_load_template.html'
            response = HttpResponse()
            items_html = render_to_string(
                template_name,
                    {'items': queryset, 'remaining_count': remaining_count, 'load_ids': load_ids, 'count': loaded_count, 'is_odd': is_odd, }
            )
            response.content = items_html
            return response

items_loader_by_ids = ItemsByIdLoaderView.as_view()

