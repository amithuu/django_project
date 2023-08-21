from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
)       
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


  #[ we are taking this to make the posts in a list view]

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




class PostListView(ListView):  
    # we have created a class , because these are class based view..
    model = Post
    template_name= 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # this is the name of the class that will be created for the post list view[how we have a variable in home function 'posts' in the same way we create the a object variable for class to know that it has its variable to get the objects.
    paginate_by = 1  # this is the number of posts that we want to display per page.
    ordering = ['-date_posted']  # this is the order of the posts that we want to display.[newest first]


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):  # As for the Classes we cannot add decoretors eg:[@loginrequired], So we use this *LoginRequiredMixin* 
    model= Post
    fields = ['title', 'content']

    # even after creating post, we are not telling for which user the post has to be created??
    # [to tell for the current logged in user, we have a function called "*form_valid()*"]
    def form_valid(self, form):
        form.instance.author = self.request.user  # this will add the instance of the current logged in user..
        return super().form_valid(form)           # we are setting that the form is valid to execute.. 
      


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # UserPassesTestMixin: this the method wchich checks for the current logged in user.
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # the below function test_func() is used to check wheter the current logged in user and author of the post is "SAME", or not[if same == allow,, else: 403 error[forbidden]]//
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # <Error> # No URL to redirect to. Provide a success_url  [when user click on delete button if we have not given the success_url ]
    success_url='/' # redirect to home page after deletion of the post, 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request, 'blog/about.html',{'title':'learning django'})
