from django.contrib.auth.models import BaseUserManager
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
        data.set_password(password)
        data.save()

        return data 

    def create_superuser(self, username, email, password):

        data = self.create_user(username, email, password)
        data.is_superuser = True
        data.is_staff = True
        data.is_active = True
        data.save()
        
        return data
    
    # def update_password(self, id, new_password):
    #     if id is None:
    #         raise TypeError("Your ID not found to our database")
        
    #     if new_password is None:
    #         raise TypeError("New password must be filled")

    #     check = self.model.get(id=id)
    #     check.password = new_password
    #     check.save()

    #     return check

class VerifyCodeManager(BaseUserManager):
    def create_code(self, user_id:Optional[str], code, created=None, updated=None):
        if code is None:
            raise TypeError("Code is important field")
        
        data = self.model(user_id=user_id, code=code, created=created)
        data.save()
