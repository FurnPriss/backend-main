from datetime import *
from rest_framework.views import APIView
from functional import response_bad_request, response_not_found, trvStore, delete_cookie
from .serializers import CodeSerializers
from passlib.hash import sha256_crypt

# Create your views here.
class VerifyCode(APIView):
    def patch(self, request):
        data = {
            "token": request.data["token"]
        }
        obj = trvStore()
        parser = CodeSerializers(data=data)

        if parser.is_valid():
            existing_code = obj.search_validation_code(data["token"])
            if existing_code is None:
                return response_not_found(404, "Please check your inbox to verify code")
            
            date_now = datetime.now()
            new_password = sha256_crypt.hash(request.COOKIES["password"])
            require_tbl_token = [date_now, data["token"]]
            require_updt_psw = [new_password, existing_code["user_id_id"]]

            obj.update_table_token(require_tbl_token)
            obj.update_password(require_updt_psw)
            return delete_cookie(201, "Password has been updated", "password")

        return response_bad_request(400, "Fill must be valid")
