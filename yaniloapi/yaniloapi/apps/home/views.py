from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from yaniloapi.settings import contains
from . import models
from .serializers import BannerModelSerializer, NavModelSerializer, BottomModelSerializer


class BannerView(ListAPIView):
    """
    轮播图api
    """
    queryset = models.Banner.objects.filter(is_deleted=False, is_show=True)[0:contains.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class NavView(ListAPIView):
    """
    导航栏api
    """
    queryset = models.Nav.objects.filter(is_deleted=False, is_show=True, position=1)[0:contains.NAV_TOP_LENGTH]
    serializer_class = NavModelSerializer


class BottomView(ListAPIView):
    """
    导航栏api
    """
    queryset = models.Nav.objects.filter(is_deleted=False, is_show=True, position=1)[0:contains.NAV_TOP_LENGTH]
    serializer_class = BottomModelSerializer