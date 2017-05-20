# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from forms import UrlForm
from shortner.controls import *
from yaus_main.globals import *


def index(request):
    """This view renders the front page"""

    form = UrlForm()
    messages = {'success': "", 'errors': []}

    # If user submits the form, this view will be triggered also, and this condition will be triggered
    if request.method == 'POST':
        long_url = request.POST['long_url']
        custom_url = request.POST['custom_url']
        already_used = False
        valid_url = False

        if is_valid_url(long_url):
            valid_url = True

            if custom_url is not None and len(custom_url) > 0:
                qs = get_original(custom_url)
                if qs is not None and qs.first() is not None:
                    messages['errors'].append('Custom URL is already used!')
                    already_used = True

        if not valid_url:
            messages['errors'].append('Invalid URL!')

        elif not already_used:
            short_url = shorten(long_url, custom_url=custom_url)
            messages['success'] = short_url

    return render(request, "index.html", {'url_form': form, 'messages': messages})


def redirector(request):
    short_url = request.get_raw_uri().split('/')[-1]
    record = get_original(short_url, increment_visits=True)

    if record is not None and record.first() is not None:
        long_url = record.first().long_url

        if not ((len(long_url) > 7 and long_url[0:8] == "https://") or (len(long_url) >= 7 and long_url[0:7] == "http://")):
            long_url = "http://" + long_url
    else:
        return render(request, "404.html", {'messages': {'errors': ['This URL is not valid, where did you get it from?', 'dont try to be slick']}})

    return redirect(long_url, permanent=True)


def view_all(request):
    all_urls = get_all()
    for url in all_urls:
        url.short_url = domain+"/"+url.short_url

    data = {
        'short_urls': all_urls,
    }
    return render(request, "links.html", data)


def invalid_url(request):
    return render(request, "404.html", {'messages': {'errors': ['This URL is not valid, where did you get it from?', 'dont try to be slick']}})
