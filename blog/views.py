from django.shortcuts import render
from .models import Post #.models= it is in same folder


# from django.http import HttpResponse

post=[
        {
            'author':'kp singh',
            'title':'Blog Post 1',
            'content':'First Post content',
            'date_posted':'August 27, 2018',

        },
        {
            'author':'jatin',
            'title':'Blog Post 2',
            'content':'Second Post content',
            'date_posted':'August 28, 2018',

        },
    ]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render (request,'blog/home.html',context)

def about(request):
    return render (request,'blog/about.html',{'title':'About'})


# Create your views here.
