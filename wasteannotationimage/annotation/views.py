from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from annotation.models import Image
from .forms import NewImage

def mainpage(request):
    images = Image.objects.all()
    return render(request, 'annotation/mainpage.html', {'imagesObj': images})

def about(request):
    return render(request, 'annotation/about.html', locals())

def newImage(request):
    isSave = False
    form = NewImage(request.POST or None, request.FILES)
    if form.is_valid():
        image = Image()
        image.name = form.cleaned_data["name"]
        image.image = form.cleaned_data["image"]
        image.save()
        isSave = True
        #return redirect('newimage')

    return render(request, 'annotation/newImage.html', locals())



# Create your views here.
