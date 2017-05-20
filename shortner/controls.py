from .models import *
from serializer.serializers.number_serializer import *
from serializer.serializers.random_serializer import *
from yaus_main.globals import *
import re



def is_valid_url(url):
    r_expression = r'^(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})$'
    match = re.match(r_expression, url) 
    if match is not None:
        return True
    return False



def create_url(serial):
    return domain + "/" + str(serial)


# def shorten(url):
#     serial = unicode(NumberSerializerEngine.get_new_serial())
#     shortened_url = ShortUrl(short_url=serial, long_url=url)
#     shortened_url.save()
#     return create_url(serial)


def shorten(url, custom_url=None):
    serial = ""

    if custom_url is None or len(custom_url) == 0:
        serial = unicode(RandomSerializerEngine.get_new_serial())
    else:
        serial = custom_url

    shortened_url = ShortUrl(short_url=serial, long_url=url)
    shortened_url.save()
    
    return create_url(serial)


def get_all():
    return ShortUrl.objects.all()


def get_original(short_url, increment_visits=False):

    if increment_visits:
        increment(short_url)

    short_url = ShortUrl.objects.filter(short_url=short_url)
    return short_url


def increment(short_url):
    short_url = ShortUrl.objects.filter(short_url=short_url)

    if short_url is not None and short_url.first() is not None:
        short_url = short_url.first()
        short_url.visits += 1
        short_url.save()
