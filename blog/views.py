from django.shortcuts import render
from django.http import HttpResponse


# this was the one way were we can use the apps to open[using HttpResponce]

# def home(request):
#     return HttpResponse("<h1> hi this is home page </h1>")

# def about(request):
#     return HttpResponse("<h1> hi this is about page </h1>")

# an another way using render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request,'blog/about.html')