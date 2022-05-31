from django.contrib.auth.models import BaseUserManager
from passlib.hash import sha256_crypt
from typing import Optional

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):

        if username is None:
            raise TypeError("User must have a username")
        
        if email is None:
            raise TypeError("User must have a email")
        
        if password is None:
            raise TypeError("User must have a password")

        data = self.model(username=username, email=email)
        data.set_password(sha256_crypt.hash(password))
        data.save()

        return data 

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError("Superuser must have a password")

        data = self.create_user(username, email, sha256_crypt.hash(password))
        data.is_superuser = True
        data.is_staff = True
        data.is_active = True
        data.save()
        
        return data

class VerifyCodeManager(BaseUserManager):
    def create_code(self, user_id:Optional[str], code, created=None, updated=None):
        if code is None:
            raise TypeError("Code is important field")
        
        data = self.model(user_id=user_id, code=code, created=created)
        data.save()
    