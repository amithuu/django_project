# we are taking all the paths here and adding the link to other files..

from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="blog-home"),
    path('about/', views.about, name='blog-about'),
]