# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ShortUrl(models.Model):
    # The original URL, max length is 255 so that no one inserts dump data into db and cause problems
    long_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=10)
    time_stamp = models.DateField(auto_now=True)

    def __str__(self):
        return "[" + self.long_url + " => " + self.short_url + "]"