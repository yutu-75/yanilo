import re

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers
from rest_framework_jwt.compat import get_username_field, PasswordField
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings
from . import models
from django.contrib.auth.hashers import make_password
from django_redis import get_redis_connection

from .utils import get_user_obj

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomeSerializer(JSONWebTokenSerializer):

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)
        self.fields['ticket'] = serializers.CharField(write_only=True)
        self.fields['randstr'] = serializers.CharField(write_only=True)

    #
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password'),
            'ticket': attrs.get('ticket'),
            'randstr': attrs.get('randstr'),
        }
        # {'username':'root',password:'123'}

        if all(credentials.values()):

            user = authenticate(self.context['request'], **credentials)  # self.context['request']当前请求的request对象

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class RegisterModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    sms = serializers.CharField(max_length=6, min_length=4, write_only=True)  # '3333'
    r_password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  #

    class Meta:
        model = models.User
        fields = ['id', 'phone', 'password', 'r_password', 'sms', 'token']
        extra_kwargs = {
            'password': {'write_only': True},
        }


    # 校验密码和确认密码
    def validate(self, attrs):
        # 校验手机号
        print('>>>>>',attrs)
        phone_number = attrs.get('phone')
        sms = attrs.get('sms')
        phone_number = '15025555653'
        if not re.match('^1[3-9][0-9]{9}$', phone_number):
            raise serializers.ValidationError('手机号格式不对')

        ret = get_user_obj(phone_number)
        if ret:
            raise serializers.ValidationError('has one!!!')
        p1 = attrs.get('password')
        p2 = attrs.get('r_password')
        if p1 != p2:
            raise serializers.ValidationError('两次密码不一致，请核对')

        # todo  校验验证码
        conn = get_redis_connection('sms_code')
        ret = conn.get('mobile_%s'%phone_number)
        if not ret:
            raise serializers.ValidationError('验证码已失效')
        if ret.decode() != sms:
            raise serializers.ValidationError('验证码 youwu')


        return attrs

    def create(self, validated_data):

        validated_data.pop('r_password')
        validated_data.pop('sms')
        # 密码加密
        hash_password = make_password(validated_data['password'])
        validated_data['password'] = hash_password

        validated_data['username'] = validated_data.get('phone')

        user = models.User.objects.create(
            **validated_data
        )


        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        user.token = token


        return user
