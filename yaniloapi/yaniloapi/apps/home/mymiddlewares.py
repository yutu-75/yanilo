from django.shortcuts import  HttpResponse,render,redirect
from django.utils.deprecation import MiddlewareMixin
class Auth(MiddlewareMixin):
    def process_request(self, request):
        return None

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = "content-type"
        response['Access-Control-Allow-Methods'] = "DELETE,PUT"
        return response










