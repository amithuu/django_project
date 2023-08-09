from django.shortcuts import render

# this was the one way were we can use the apps to open[using HttpResponce]
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1> hi this is home page </h1>")

# def about(request):
#     return HttpResponse("<h1> hi this is about page </h1>")

# an another way using render
#[ we try to pass some dummpy data and check ]

####################################################################################

# posts = [
#     {
#         'author': 'Amith',
#         'title': 'Learning Django',
#         'dateposted': 'Today',
#         'content': 'this is Django learning time!!!'
#     },
#     {
#         'author': 'Sudesh',
#         'title': 'Learning Django',
#         'dateposted': 'Dont Know',
#         'content': 'this is Django learning time!!!'
#     }
# ]



# def home(request):
#     context={
#         'posts':posts
#     }
#     return render(request, 'blog/home.html',context)

# def about(request):
#     context={
#         'posts':posts
#     }
#     return render(request,'blog/about.html',{'title':'learning django'})

#   # the "render function" accepts only 3 parameter, so if there is title, we cannot pass context as in about page I have passed only title not context.

#####################################################################################################################
# We used the dummy data in the above example so now , trying to get from database which is created.[as we have created our db in "models", so we are importing the "models.Post" class as well]

from .models import Post

def home(request):
    context = {
        'posts':Post.objects.all()  # the attributes from the above posts and the from the templates should be same!![if not please change it in templates page.]
                                                            # [once db is creted with the new data, we can remove the dummy data.]
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'learning django'})
