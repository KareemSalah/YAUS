# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from forms import UrlForm
from shortner.controls import *


def index(request):
    """This view renders the front page"""

    form = UrlForm()
    messages = {'success': "", 'errors': []}

    # If user submits the form, this view will be triggered also, and this condition will be triggered
    if request.method == 'POST':
        long_url = request.POST['long_url']
        # The URL might be validated here before shortening
        short_url = shorten(long_url)
        messages['success'] = short_url

    return render(request, "index.html", {'url_form': form, 'messages': messages})


def redirector(request):
    # TODO: implement
    return render(request, "index.html", {})
