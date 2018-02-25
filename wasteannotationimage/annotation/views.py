from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

def mainpage(request):
    return render(request, 'annotation/mainpage.html', locals())

# Create your views here.
