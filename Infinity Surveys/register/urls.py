from django.contrib import admin
from django.urls import path, include 
from .views import UserEditView

urlpatterns = [
    path('profile/', UserEditView.as_view(), name='profile')
]