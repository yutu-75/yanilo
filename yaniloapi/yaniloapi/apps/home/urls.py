from django.urls import path, include
from . import views


urlpatterns = [
    path(r'banner/', views.BannerView.as_view()),
    path(r'nav/', views.NavView.as_view()),
    path(r'bottom/', views.BottomView.as_view())
]