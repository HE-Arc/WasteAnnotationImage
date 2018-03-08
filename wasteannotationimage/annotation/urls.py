from django.urls import path
from . import views

urlpatterns = [
    path('mainpage', views.mainpage, name='mainpage'),
    path('about', views.about, name='about'),
    path('newimage', views.newImage, name='newimage'),
    ]
