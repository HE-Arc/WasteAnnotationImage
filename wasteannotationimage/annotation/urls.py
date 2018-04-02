from django.urls import path
from . import views

urlpatterns = [
    path('home', views.mainpage, name='mainpage'),
    path('about', views.about, name='about'),
    path('newimage', views.newImage, name='newimage'),
    path('annotationImage/<int:id>', views.annotationImage, name='annotationImage'),
    path('', views.redirectionLogin, name='redirectionLogin'),
    ]
