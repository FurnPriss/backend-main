from django.db import models

# Create your models here.
class EndUser(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self): 
        return f"Username has been filled: {self.username}"