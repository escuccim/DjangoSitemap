# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page,Sitemap,SitemapImage
# Register your models here.

class ImageInline(admin.TabularInline):
    model = SitemapImage
    extra = 3

class PageAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Page, PageAdmin)
admin.site.register(Sitemap)