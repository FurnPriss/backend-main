from django.urls import path
from .views import RegistrationViewAPI, VerifyCodeAPI

app_name='user'

urlpatterns = [
    path('sys-regis/', RegistrationViewAPI.as_view(), name='register'),
    path('sys-reset-psw/', VerifyCodeAPI.as_view(), name='reset')
]