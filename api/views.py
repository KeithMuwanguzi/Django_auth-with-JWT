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
        user = ser.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'Token': token.key, 'user_data': ser.data}, status=201)
    else:
        return Response({"Response": "An error occurred", "errors": ser.errors}, status=400)