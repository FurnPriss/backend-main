from rest_framework.views import APIView
from functional import response_bad_request, response_not_found, set_cookie, trvStore
from .serializers import ResetPassword
from functional import trvStore
from django.core.mail import send_mail
import shortuuid
from datetime import *

# Create your views here.
class resetPassword(APIView):
    def post(self, request):
        random = shortuuid.ShortUUID().random(length=5)
        subject = "Reset Password"
        msg = f"Don't publish your verification code whatever the reason\nYour verify code: {random}"

        data = {
            "email": request.data["email"],
            "password": request.data["password"],
            "confirm_password": request.data["confirm_password"]
        }
        parser = ResetPassword(data=data)
        obj = trvStore()
        checking_email = obj.email_exist(data["email"])

        if data["password"] != data["confirm_password"]:
            return response_bad_request(400, "Password must be same with confirm field")
        
        if checking_email is None:
            return response_not_found(404, "Email isn't available on our database")
        
        if parser.is_valid():
            row = [random,datetime.now(),checking_email['id']]
            obj.insert_codeV(row)
            send_mail(subject, msg, 'akhmadfaizal13@gmail.com',[checking_email["email"]], fail_silently=False)
            return set_cookie(201, "We sent email to you. Please check your inbox", "password", data["password"])
        
        return response_bad_request(400, "Please complete field on form")