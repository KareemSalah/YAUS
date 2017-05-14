from django.conf.urls import url, include
from .views import *
from shortner.models import ShortUrl
from rest_framework import routers, serializers, viewsets


class ShortUrlSerializer(serializers.Serializer):
    short_url = serializers.CharField(max_length=10)
    long_url = serializers.CharField(max_length=255)


class ShortUrlViewSet(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer


router = routers.DefaultRouter()
router.register(r'getall', ShortUrlViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^shorten/$', shorten),
    # url(r'^getall/$', get_all),
    # url(r'^getorig/$', get_original),
    # url(r'^$', api_guide),
    # url(r'^', invalid_url),
]
