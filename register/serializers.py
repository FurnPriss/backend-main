from rest_framework import serializers
from .models import EndUser

class UsersForm(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = EndUser
        fields = ('__all__')