from django.urls import path

from expenses.views import expense_create

urlpatterns = [
    path('expenses/', expense_create),  
]