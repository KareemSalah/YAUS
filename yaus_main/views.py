# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from forms import UrlForm
from shortner.controls import *
from shortner.models import ShortUrl

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
    short_url = request.get_raw_uri().split('/')[-1]
    record = ShortUrl.objects.filter(short_url=short_url).first()

    if record is not None:
        long_url = record.long_url
    else:
        return render(request, "404.html", {'messages': {'errors': ['This URL is not valid, where did you get it from?', 'dont try to be slick']}})

    return redirect(long_url, permanent=True)


def invalid_url(request):
    return render(request, "404.html", {'messages': {'errors': ['This URL is not valid, where did you get it from?', 'dont try to be slick']}})
