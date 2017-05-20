# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .controls import *
import json


@csrf_exempt
def api_shorten(request):
    if request.POST is None or (request.POST is not None and 'long_url' not in request.POST):
        return json_response(request, json_data={'errors': ['invalid post request']})

    # TODO: this could lead to sql injection, sanitize first
    # TODO: check if the url is valid
    long_url = request.POST['long_url']
    custom_url = request.POST['custom_url']
    already_used = False
    valid_url = False
    json_data = {'errors': []}

    if is_valid_url(long_url):
        valid_url = True

        if custom_url is not None and len(custom_url) > 0:
            qs = get_original(custom_url)
            if qs is not None and qs.first() is not None:
                json_data['errors'].append('Custom URL is already used!')
                already_used = True
        if not valid_url:
            messages['errors'].append('Invalid URL!')

        elif not already_used:
            short_url = shorten(long_url, custom_url=custom_url)
            json_data['success'] = 'yes'
            json_data['short_url'] = short_url

    return json_response(request, json_data=json_data)


@csrf_exempt
def api_get_all(request):
    all_urls = get_all()
    json_data = {'success': 'yes', 'urls': []}

    for url in all_urls:
        json_data['urls'].append({'short_url': url.short_url, 'long_url': url.long_url, 'visits': url.visits})

    return json_response(request, json_data)


@csrf_exempt
def api_get_original(request):
    json_data = {}

    if request.POST is None or (request.POST is not None and 'short_url' not in request.POST):
        return json_response(request, json_data={'errors': ['invalid post request']})

    # TODO this could lead to sql injection, sanitize this first
    serial = request.POST['short_url'].split('/')[-1]

    long_url = get_original(short_url=serial)

    if long_url is None or long_url.first() is None:
        json_data = {'errors': ['this url is not in database']}
        return json_response(request, json_data)

    long_url = long_url.first().long_url
    json_data = {'success': 'yes', 'long_url': long_url}
    return json_response(request, json_data)


@csrf_exempt
def api_invalid_url(request):
    return json_response(request, json_data={'errors': ['invalid api url']})


@csrf_exempt
def api_guide(request):
    guide = {
        '/api/shorten/': {
            'description': 'minifies a long url <= 255 characters long',
            'parameters': {
                'long_url': 'string <= 255 characters length',
            }
        },
        '/api/getall/': {
            'description': 'gets all urls and their long urls in database',
        },
        '/api/getorig/': {
            'description': 'get original long url for a given short url',
            'parameters': {
                'short_url': 'the short url ending in a string of digits'
            }
        }
    }
    return json_response(request, json_data=guide)


def json_response(request, json_data={}):
    return render(request, "json.html", {'json_data': json.dumps(json_data)})
