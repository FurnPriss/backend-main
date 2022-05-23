from functional import response_bad_request, response_internal_server, response_success_ok, trvStore
from rest_framework.views import APIView
from .serializers import UsersForm
from passlib.hash import sha256_crypt

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

        if len(request.data["password"]) < 8 or len(request.data["username"]) < 6:
            return response_bad_request(400, "There is an error related to the form. Please check carefully")

        if parser.is_valid():
            query = obj.email_exist(data['email'])
            if query is None:
                looping = [x for x in data.values()]
                obj.insert_enduser(looping)
                return response_success_ok(201, "You've created a new account")

            return response_internal_server(500, 'Email has been used')

        return response_bad_request(400, 'Please fill your data to each of fields')