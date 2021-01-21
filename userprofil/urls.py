from django.urls import path
from .views import user_profile, delete, comment_list

urlpatterns = [
    path('profil/', user_profile, name='user_profile'),
    path('yorumlar/', comment_list, name='comment_list'),
    path('profile/delete/<id>', delete, name='delete'),
]
