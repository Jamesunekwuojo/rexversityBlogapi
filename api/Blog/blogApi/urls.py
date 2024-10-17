from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.getBlog, name="get-blog"),  # To Get all blogs
    path("blogposts/create/", views.createBlog, name="create-blog"),  # To Create a new blog post
    path("blogposts/<int:pk>/", views.updateBlog, name="update-blog"),  #To  Update a blog post by ID
    path("blogposts/<int:pk>/delete/", views.deleteBlog, name="delete-blog"),  # Yo Delete a blog post by ID
]
