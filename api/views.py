from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from . serializers import UserSerializer 
from rest_framework.response import Response 

@api_view(["POST"])
def login(request):
    user = get_object_or_404(User, username = request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({
            'message':'The details you entered do not match an active user',
            'status':'error'
        })
    else:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance = user)
        return Response({
            'token':token.key,
            'data':serializer.data
        })

@api_view(['POST'])
def signUp(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        serializer = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message':'User created successfully',
            'data':{
                'token':token.key,
                'data':serializer.data
            },
            'status':'success'
        })
    else:
        return Response({
            'message':'An error occured',
            'error':serializer.errors,
            'status':'error'
        })
    

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({
        'message':'Users fetched successfully',
        'data': serializer.data,
        'status':'success'
    })
