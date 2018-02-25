from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

def login(request):

    return render(request, 'account/login.html', locals())

# Create your views here.
