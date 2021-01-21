from django.urls import path
from .views import  explore
urlpatterns = [

    path('keşfet/', explore, name='explore'),

]