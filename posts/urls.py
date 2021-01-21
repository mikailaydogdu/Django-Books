from django.urls import path
from .views import posts, posts_details
urlpatterns = [
    path('posts/', posts, name='posts'),
    path('posts_details/<slug>', posts_details, name='posts_details'),
]