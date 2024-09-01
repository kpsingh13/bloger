from django.shortcuts import render
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
        'posts':post
    }
    return render (request,'blog/home.html',context)

def about(request):
    return render (request,'blog/about.html',{'title':'About'})


# Create your views here.
