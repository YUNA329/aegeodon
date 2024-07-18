from django.urls import path
from users.views import user_register, user_login, user_detail

urlpatterns = [
    path('users/signup', user_register),
    path('users/login', user_login),
    path('users/', user_detail),
]