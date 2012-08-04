# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.mainblock.models import License,Person,Purchase,PurchaseAttachedDoc,Document
from sorl.thumbnail.admin import AdminImageMixin
from apps.utils.widgets import Redactor


class LicenseAdmin(admin.ModelAdmin, AdminImageMixin):
    list_display = ('id','title','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    search_fields = ('title',)

admin.site.register(License, LicenseAdmin)

class DocumentAdmin(admin.ModelAdmin, AdminImageMixin):
    list_display = ('id','title','create_date','is_published',)
    list_display_links = ('id','title','create_date',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('title',)

admin.site.register(Document, DocumentAdmin)

class PersonAdmin(admin.ModelAdmin, AdminImageMixin):
    list_display = ('id','fullname','post_title','order','is_published',)
    list_display_links = ('id','fullname','post_title',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    search_fields = ('fullname','post_title','phone_num',)

admin.site.register(Person, PersonAdmin)

class PurchaseDocInline(admin.TabularInline):
    model = PurchaseAttachedDoc

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id','title','type','date_create','is_published',)
    list_display_links = ('id','title','type','date_create',)
    list_editable = ('is_published',)
    search_fields = ('title','price',)
    list_filter = ('date_create','is_published',)
    inlines = [PurchaseDocInline]

admin.site.register(Purchase, PurchaseAdmin)
