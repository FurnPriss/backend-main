from rest_framework import serializers
from forgetted_password.models import TokenConfirm

class CodeSerializers(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255)

    class Meta:
        model = TokenConfirm
        fields = ('token',)