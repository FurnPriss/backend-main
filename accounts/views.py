from rest_framework.views import APIView
from .serializers import UserRegistration, UserModel, ResetPassword, VerifyCodeModel
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
from dotenv import load_dotenv
import shortuuid
from datetime import *
import re, os

load_dotenv(dotenv_path='./.env')
# Create your views here.
class RegistrationViewAPI(APIView):

    def __init__(self):
        self.serializer = UserRegistration
    
    def post(self, request):
        data = {
            "username": request.data['username'],
            "email": request.data['email'],
            "password": request.data['password']
        }

        serializer = self.serializer(data=data)
        pattern =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
        regex = re.fullmatch(pattern, data["email"])

        if serializer.is_valid():
            if not regex:
                return Response({"email": "Email must have a pattern '.com'"},status=status.HTTP_400_BAD_REQUEST)

            UserModel.objects.create_superuser(data["username"], data["email"], data["password"])

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyCodeAPI(APIView):
    def __init__(self):
        self.reset = ResetPassword

    def post(self, request):
        random = shortuuid.ShortUUID().random(length=5)
        age = 365*24*60*60
        subject = "Reset Password"
        msg = f"Don't publish your verification code whatever the reason\nYour verify code: {random}"

        data = {
            "email": request.data["email"],
            "password": request.data["password"],
            "confirm_password": request.data["confirm_password"]
        }

        retrive = self.reset(data=data)
        exist_email = UserModel.objects.filter(email=data["email"]).exists()
        choice_email = UserModel.objects.filter(email=data["email"]).values("id", "email")

        if data["password"] != data["confirm_password"]:
            return Response({"message": "Please correct, password and confirm password must be same"},status=status.HTTP_404_NOT_FOUND)

        if retrive.is_valid():

            if exist_email:
                VerifyCodeModel.objects.create_code(user_id=choice_email[0]["id"], code=random)
                send_mail(subject, msg, os.getenv("EMAIL"),[choice_email[0]["email"]], fail_silently=False)
                response= Response({"message": "We sent email to you. Please check your inbox"}, status=status.HTTP_201_CREATED)
                response.set_cookie(key="password", value=data["password"], httponly=False, expires=datetime.now() + timedelta(seconds=age), max_age=age)
                return response
            else:
                return Response(
                    {
                        "message": "Email isn't available on our database"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        
        return Response(retrive.errors, status=status.HTTP_400_BAD_REQUEST)


        
        