from functional import response_bad_request, response_internal_server, response_success_ok, trvStore
from rest_framework.views import APIView
from .serializers import UsersForm
from passlib.hash import sha256_crypt
from .models import EndUser

# Create your views here.
class APIRegister(APIView):
    def post(self, request):
        data = {
            'email':request.data['email'],
            'name': request.data['name'],
            'username': request.data['username'],
            'password': sha256_crypt.hash(request.data['password'])
        }
        obj = trvStore()
        parser = UsersForm(data=data)

        if parser.is_valid():
            query = obj.email_exist(data['email'])
            if query is None:
                looping = [x for x in data.values()]
                obj.insert_enduser(looping)
                return response_success_ok(200, 'Sign Up has been successfully')

            return response_internal_server(500, 'Email has been used')

        return response_bad_request(400, 'Please fill your data to each of fields')