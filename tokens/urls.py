from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from tokens.apps import TokensConfig

app_name = TokensConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
]
