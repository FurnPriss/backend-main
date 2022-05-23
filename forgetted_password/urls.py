from django.contrib import admin
from django.urls import path
from .views import resetPassword

app_name='forget'

urlpatterns = [
    path('sys-reset-psw/', resetPassword.as_view(), name='reset_psw'),
]