from rest_framework import serializers
from register.models import EndUser

class ResetPassword(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=8)
    confirm_password = serializers.CharField(max_length=255, min_length=8)

    class Meta:
        model = EndUser
        fields = ("email", "password", "confirm_password",)
