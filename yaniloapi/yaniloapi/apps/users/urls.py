from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from . import views
from django.urls import path,re_path

urlpatterns = [

    path(r'login/', views.CustomLoginView.as_view()),  #颁发token值的
    path(r'verify/', verify_jwt_token),
    path(r'check_phone/', views.CheckPhoneNumber.as_view()),
    path(r'register/', views.RegisterView.as_view()),
    re_path(r'sms_code/(?P<phone>1[3-9][0-9]{9})/', views.GetSMSCodeView.as_view()),
]