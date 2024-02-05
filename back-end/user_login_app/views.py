from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import User
from tracker_library_app.models import TrackerLibrary
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class Master_Sign_Up(APIView):

    def post(self, request):
        username = request.data.get("email")
        master_user = User.objects.create_user(username, request.data.get("email"), request.data.get("password"))
        master_user_library = TrackerLibrary(user=master_user)
        master_user.is_staff = True
        master_user.is_superuser = True
        master_user.save()
        master_user_library.save()
        token = Token.objects.create(user=master_user)
        response = JsonResponse(
            {"master_user": master_user.email, 'token' : token.key}, status=HTTP_201_CREATED
        )
        response.set_cookie(key='token', value=token.key, httponly=True)
        return Response

class Sign_Up(APIView):

    def post(self, request):
        username = request.data.get("email")
        new_user = User.objects.create_user(username, username, request.data.get("password"))
        new_user_library = TrackerLibrary(user=new_user)
        token = Token.objects.create(user=new_user)
        new_user.save()
        new_user_library.save()
        response = JsonResponse(
            {"user" : new_user.email, 'token' : token.key}, status=HTTP_201_CREATED
        )
        response.set_cookie(key='token', value=token.key, httponly=True)
        return response
    
class Log_In(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            response = JsonResponse({"user": user.email, "token": token.key})
            response.set_cookie(key='token', value=token.key, httponly=True)
            return response
        else:
            return Response("No User matches these credentials", status=HTTP_404_NOT_FOUND)

class Log_Out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        response = Response('it worked', status=HTTP_204_NO_CONTENT)
        response.delete_cookie(key='token')  # Delete the HTTP-only cookie upon logout
        return response

class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})