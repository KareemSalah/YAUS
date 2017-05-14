# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt

from yaus_main.globals import *
from django.shortcuts import render
from .controls import *
import json


def create_url(serial):
    return domain + "/" + str(serial)


@csrf_exempt
def shorten(request):
    if request.POST is None:
        return json_response(request, json_data={'errors': ['invalid post request']})


@csrf_exempt
def get_all(request):
    pass


@csrf_exempt
def get_original(request):
    print(request.POST)
    json_data = {}

    if request.POST is None or (request.POST is not None and request.POST['short_url'] is None):
        return json_response(request, json_data={'errors': ['invalid post request']})

    long_url = ShortUrl.objects.filter(short_url=request.POST['short_url'][0])

    if long_url is None:
        json_data = {'errors': ['this url is not in database']}
        return json_response(request, json_data)

    long_url = long_url.first().long_url
    json_data = {'success': 'yes', 'long_url': long_url}
    return json_response(request, json_data)


@csrf_exempt
def invalid_url(request):
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
