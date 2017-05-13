# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class NumberSerializer(models.Model):
    url_num = models.IntegerField()
    last_updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return "Current number is: " + self.url_num + ", last updated on: " + self.last_updated_on
