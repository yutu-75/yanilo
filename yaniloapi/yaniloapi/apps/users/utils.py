from urllib.parse import urlencode
import json, urllib
from urllib.request import urlopen

import requests
from django.conf import settings
from users import models
from django.db.models import Q
from yaniloapi.settings import contains

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'id':user.id,
        'credit':user.credit,
        'credit_to_money':contains.CREDIT_MONEY,
    }





def get_user_obj(accout):  # 666
    try:
        user_obj = models.User.objects.get(Q(username=accout) | Q(phone=accout))
    except:
        return None
    return user_obj


from django.contrib.auth.backends import ModelBackend

import logging

logger = logging.getLogger('django')


class CustomeModelBackend(ModelBackend):
    '''
        '
        'ticket': attrs.get('ticket'),
        'randstr': attrs.get('randstr'),

    '''

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_obj = get_user_obj(username)
            if kwargs.get('ticket'):

                ticket = kwargs.get('ticket')

                userip = request.META['REMOTE_ADDR']
                randstr = kwargs.get('randstr')
                print('userip:', userip)
                '''
                https://captcha.tencentcloudapi.com/?Action=DescribeCaptchaResult
                &CaptchaType=9
                &Ticket=xxxx
                &UserIp=127.0.0.1
                &Randstr=xxx
                &CaptchaAppId=201111111
                &AppSecretKey=xxxxxx

                '''

                # ----------------------------------
                # 腾讯验证码后台接入demo
                # ----------------------------------

                # ----------------------------------
                # 请求接口返回内容
                # @param  string appkey [验证密钥]
                # @param  string params [请求的参数]
                # @return  string
                # ----------------------------------
                params = {
                    "aid": settings.FSQ.get('appid'),
                    "AppSecretKey": settings.FSQ.get('app_serect_key'),
                    "Ticket": ticket,
                    "Randstr": randstr,
                    "UserIP": userip
                }
                params = urlencode(params).encode()

                url = settings.FSQ.get('URL')

                f = urlopen(url, params)

                content = f.read()
                res = json.loads(content)
                print(res)  # {'response': '1', 'evil_level': '0', 'err_msg': 'OK'}
                if res.get('response') != '1':
                    return None

            if user_obj:
                if user_obj.check_password(password):
                    return user_obj

            else:
                return None
        except Exception:
            logger.error('验证过程代码有误，请联系管理员')
            return None