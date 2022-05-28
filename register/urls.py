from django.contrib import admin
from django.urls import path
from .views import APIRegister

app_name='user'

urlpatterns = [
    path('sys-regis/', APIRegister.as_view(), name='register'),
]
