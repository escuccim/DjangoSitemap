# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Sitemap, Page
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import translation


# Create your views here.
def Index(request):
    sitemaps = Sitemap.objects.all()
    language = translation.get_language()
    return render(request, 'sitemap/sitemapindex.html', { 'sitemaps': sitemaps, 'language' : language})


def Pages(request):
    pages = Page.objects.all()
    language = translation.get_language()
    return render(request, 'sitemap/pages.html', {'pages': pages, 'language': language})