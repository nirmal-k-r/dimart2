from django.shortcuts import render


#default user model is used for authentication for Rest api
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from rest_framework.views import APIView
from .serialiser import AuthenticationSerialiser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


# Create your views here.
class LoginView(APIView): #login
    serializer_class=AuthenticationSerialiser
    authentication_classes=[TokenAuthentication]

    # def post(self,request):
    #     serializer=AuthenticationSerialiser(data=request.data)
    #     if serializer.is_valid():
    #         user=authenticate(username=serializer.data['username'],password=serializer.data['password'])
    #         if user is not None:
    #             # login(request,user)
    #             token,created=Token.objects.get_or_create(user=user)

    #             return JsonResponse({'message':'Login successful','token':token.key})
    #         else:
    #             return JsonResponse({'message':'Login failed'})
    #     else:
    #         return JsonResponse({'message':'Login failed. Invalid data'})

    def post(self,request):

        username=request.data['username']
        password=request.data['password']
        user=authenticate(username=username ,password=password)
        if user is not None:
            # login(request,user)
            token,created=Token.objects.get_or_create(user=user)

            return JsonResponse({'message':'Login successful', 'user': {'username':user.username, 'token':token.key}})
        else:
            return JsonResponse({'message':'Login failed'})

#register
class RegisterView(APIView):
    serializer_class=AuthenticationSerialiser
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        serializer=AuthenticationSerialiser(data=request.data)
        if serializer.is_valid():
            user=User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'])
            user.save()
            return JsonResponse({'message':'User created'})
        else:
            return JsonResponse({'message':'User creation failed'})