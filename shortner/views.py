# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from yaus_main.globals import *
from django.shortcuts import render
from .controls import *
import json


def create_url(serial):
    return domain + "/" + str(serial)


def shorten(request):
    if request.POST is None:
        return json_response(request, json_data={'errors': ['invalid post request']})


def get_all(request):
    pass


def get_original(request):
    pass


def invalid_url(request):
    return json_response(request, json_data={'errors': ['invalid url']})


def api_guide(request):
    return json_response(request, json_data={
        '/api/shorten': {
            'description': 'minifies a long url <= 255 characters long',
            'parameters': {
                'long_url': 'string <= 255 characters length',
            }
        },
        '/api/getall': {
            'description': 'gets all urls and their long urls in database',
        },
        'getorig': {
            'description': 'get original long url for a given short url',
            'parameters': {
                'short_url': 'the short url ending in a string of digits'
            }
        }
    })


def json_response(request, json_data={}):
    return render(request, "json.html", {'json_data': json.dumps(json_data)})
