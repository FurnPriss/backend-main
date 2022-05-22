from rest_framework.response import Response 
from rest_framework import status

def response_success_ok(stat, msg):
    return Response(
        {
            'status':stat,
            'message': msg
        },
        status=status.HTTP_201_CREATED
    )

def response_bad_request(stat, msg):
    return Response(
        {
            'status':stat,
            'message': msg
        },
        status=status.HTTP_400_BAD_REQUEST
    )

def response_unauthorized(stat, msg):
    return Response(
        {
            'status':stat,
            'message': msg
        },
        status=status.HTTP_401_UNAUTHORIZED
    )

def response_authorized(stat, msg):
    return Response(
        {
            'status':stat,
            'message': msg
        },
        status=status.HTTP_200_OK
    )

def response_not_found(stat, msg):
    return Response(
        {
            'status':stat,
            'message': msg
        },
        status=status.HTTP_404_NOT_FOUND
    )

def response_internal_server(stat, msg):
    return Response(
        {
            'status':stat,
            'message': msg
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )