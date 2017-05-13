from .models import *

def shorten(url):
    pass


def get_all():
    return ShortUrl.objects.all()


def get_original(short_url):
    return ShortUrl.objects.filter(short_url=short_url)
