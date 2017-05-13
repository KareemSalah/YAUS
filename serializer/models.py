# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class NumberSerializer(models.Model):
    url_num = models.IntegerField()
    last_updated_on = models.DateField(auto_now=True)

    # def __str__(self):
    #     return u"Current number is: " + unicode(str(self.url_num)) + u", last updated on: " + self.last_updated_on

    def __str__(self):
        return "Counter=" + str(self.url_num) + " LastModified=" + str(self.last_updated_on)
