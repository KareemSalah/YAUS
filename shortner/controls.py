from .models import *
from serializer.serializers.number_serializer import *
from serializer.serializers.random_serializer import *
from yaus_main.globals import *


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


def get_original(short_url):
    return ShortUrl.objects.filter(short_url=short_url)
