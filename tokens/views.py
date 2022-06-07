from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, CustomTokenVerifySerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Let's generate your jwt tokens!
    """

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Let's get a new access token!
    """

    serializer_class = CustomTokenRefreshSerializer


class CustomTokenVerifyView(TokenVerifyView):
    """
    Let's verify your token!
    """

    serializer_class = CustomTokenVerifySerializer
