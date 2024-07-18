from django.urls import path
from .views import pet_create

urlpatterns = [
    path('pets/', pet_create),
]