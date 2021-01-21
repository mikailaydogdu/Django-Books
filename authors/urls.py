from django.urls import path
from .views import author, author_details
urlpatterns = [

    path('', author, name='author'),
    path('details/<slug>', author_details, name='details'),

]