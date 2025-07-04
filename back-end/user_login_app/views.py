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
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import logging
logger = logging.getLogger(__name__)


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
        logger.info(f"Signup request data: {request.data}")
        email = request.data.get("email")
        password = request.data.get("password")
        # Input validation
        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            # Check if user already exists
            if User.objects.filter(username=email).exists():
                return Response(
                    {"error": "A user with this email already exists."},
                    status=HTTP_400_BAD_REQUEST
                )
            # Create user
            new_user = User.objects.create_user(username=email, email=email, password=password)
            token = Token.objects.create(user=new_user)

            # Create library for user
            TrackerLibrary.objects.create(user=new_user)

            # Return success response
            response = JsonResponse(
                {"user": new_user.email, "token": token.key},
                status=HTTP_201_CREATED
            )
            response.set_cookie(key='token', value=token.key, httponly=True)
            return response

        except Exception as e:
            print("Signup error:", e)  # Log to console
            return Response(
                {"error": "Something went wrong during sign-up.", "details": str(e)},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )
    
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