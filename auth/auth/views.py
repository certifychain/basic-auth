from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import userSerilizer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def signup(request):
    serializer = userSeializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({})

@api_view(['GET'])
def test_token(request):
    return Response({})