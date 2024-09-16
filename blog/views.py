from django.shortcuts import render
from .models import Post  #.models= "."here means that it is in same folder


# from django.http import HttpResponse


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render (request,'blog/home.html',context)

def about(request):
    return render (request,'blog/about.html',{'title':'About'})


# Create your views here.
