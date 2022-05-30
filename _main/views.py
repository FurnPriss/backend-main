from wsgiref.util import request_uri
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'dummy_opennotes': reverse('dummy-opennotes-list', request=request, format=format),
            'token_obtain_pair': reverse('token_obtain_pair', request=request, format=format),
            'token_refresh': reverse('token_refresh', request=request, format=format),
        })
