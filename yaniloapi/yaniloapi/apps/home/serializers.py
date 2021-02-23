from rest_framework import serializers
from . import models


class BannerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Banner
        fields = ['id', 'image_url', 'link']


class NavModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Nav
        fields = ['id', 'title', 'link', 'is_site']


class BottomModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bottom
        fields = ['']