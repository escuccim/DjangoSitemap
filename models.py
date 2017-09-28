# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Page(models.Model):
    change_freq_choices = (('yearly','yearly'),('monthly','monthly'),('weekly','weekly'),('daily','daily'))
    name = models.CharField(max_length=100)
    changefreq = models.CharField(max_length=50, choices=change_freq_choices)
    priority = models.IntegerField()
    uri = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def images(self):
        image_set = SitemapImage.objects.filter(page=self)
        return image_set

    def get_priority(self):
        return self.priority / 10

    def __unicode__(self):
        return self.name


class Sitemap(models.Model):
    uri = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.uri


class SitemapImage(models.Model):
    page = models.ForeignKey(Page)
    uri = models.CharField(max_length=100)
    caption = models.CharField(max_length=151)
    title = models.CharField(max_length=151)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


