# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Sitemap, Page
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import translation
from blog import models as blog_models
from django.conf import settings

# Create your views here.
def Index(request):
    sitemaps = Sitemap.objects.all()
    language = translation.get_language()
    languages = settings.LANGUAGES
    return render(request, 'sitemap/sitemapindex.html', { 'sitemaps': sitemaps, 'language' : language, 'languages' : languages})


def Pages(request):
    pages = Page.objects.all()
    language = translation.get_language()
    languages = settings.LANGUAGES
    return render(request, 'sitemap/pages.html', {'pages': pages, 'language': language, 'languages' : languages})


def Blog(request):
    blogs = blog_models.Blog.objects.all()
    language = translation.get_language()
    languages = settings.LANGUAGES
    return render(request, 'sitemap/blogs.html', { 'blogs' : blogs, 'language': language, 'languages' : languages })

def Label(request):
    labels = blog_models.Tag.objects.all()
    language = translation.get_language()
    languages = settings.LANGUAGES
    return render(request, 'sitemap/labels.html', {'labels': labels, 'language': language, 'languages': languages})