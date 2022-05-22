from django.db import models
from register.models import EndUser

# Create your models here.
class TokenConfirm(models.Model):
    user_id = models.ForeignKey(EndUser, on_delete=models.CASCADE, related_name='users_id')
    token = models.CharField(max_length=100, unique=True)
    confirm = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    when_confirm = models.DateTimeField(null=True)

    def __str__(self): 
        return f"Your token has been generated code"