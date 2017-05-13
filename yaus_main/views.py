# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import Http404
from forms import UrlForm


def index(request):
    """This view renders the front page"""

    form = UrlForm()
    messages = {'success': [], 'errors': []}

    # If user submits the form, this view will be triggered also, and this condition will be triggered
    if request.method == 'POST':
        # TODO
        # validate the url
        # if valid .. then convert
        # if not valid .. display an error message
        pass

    return render(request, "index.html", {'url_form': form, 'messages': messages})


def redirector(request):
    # TODO: implement
    return render(request, "index.html", {})
