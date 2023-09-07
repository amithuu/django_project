from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
)
from . import views

urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('', PostListView.as_view(), name='blog-home'), # "if we are passing the class based views we cannot pas sthe class name, we user classname.as_view()"
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # "if we are passing the class based views we cannot pass the class name, we user classname.as_view()"
    path('post/new/', PostCreateView.as_view(), name='post-create'), # 'created a new form to create new post for the user in front-end'
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]