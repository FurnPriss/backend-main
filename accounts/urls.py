from django.urls import path
from .views import RegistrationViewAPI, GenerateCodeAPI, VerifyCodeAPI

app_name='user'

urlpatterns = [
    path('sys-regis/', RegistrationViewAPI.as_view(), name='register'),
    path('sys-reset-psw/', GenerateCodeAPI.as_view(), name='reset'),
    path('sys-confirm/', VerifyCodeAPI.as_view(), name='verify')
]
