from django.contrib import admin
from django.urls import path
from .views import VerifyCode

app_name='verify'

urlpatterns = [
    path('sys-confirm/', VerifyCode.as_view(), name='code'),
]
