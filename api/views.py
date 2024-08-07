from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from . serializers import UserSerializer

@api_view(['POST'])
def login(request):
    return Response({'Response':'Under development'})

@api_view(['POST'])
def signUp(request):
    ser = UserSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
        user = User.objects.get(username = request.data['username'])
        token = Token.objects.create(user)
        return Response({'Token':token,'user_data':ser.data})
    else:
        return Response({"Response":"An error occured"})