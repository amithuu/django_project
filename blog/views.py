from django.shortcuts import render

# this was the one way were we can use the apps to open[using HttpResponce]
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1> hi this is home page </h1>")

# def about(request):
#     return HttpResponse("<h1> hi this is about page </h1>")

# an another way using render
#[ we try to pass some dummpy data and check ]

posts = [
    {
        'author': 'Amith',
        'title': 'Learning Django',
        'dateposted': 'Today',
        'content': 'this is Django learning time!!!'
    },
    {
        'author': 'Sudesh',
        'title': 'Learning Django',
        'dateposted': 'Dont Know',
        'content': 'this is Django learning time!!!'
    }
]



def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    context={
        'posts':posts
    }
    return render(request,'blog/about.html',{'title':'learning django'})

  # the "render function" accepts only 3 parameter, so if there is title, we cannot pass context as in about page I have passed only title not context.