from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
import random

class RegistrationViewSet(APIView):
    def get(self, request):
        return Response({
            "message" : "Registration(GET)"
        })
    
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class LoginViewSet(APIView):
    def get(self, request):
        return Response({
            "message": "Login(GET)"
        })
    
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not phone_number:
            return Response({
                "error" : "Phone number is required."
            })
        
        if not password:
            return Response({
                "error" : "Password is required."
            })

        user = authenticate(phone_number=phone_number, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        
        try:
            models.CustomUser.objects.get(phone_number=phone_number)
            return Response({
                "message": "Incorrect password"
            })
        except models.CustomUser.DoesNotExist:
            return Response({
                "message": "User does not exist"
            })
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({
        "message" : "This is a protected view."
    })

class RefreshView(APIView):
    def post(self, request):
        refresh = request.data.get('refresh')

        if not refresh:
            return Response({
                "error" : "Refresh token required."
            })
        
        token = RefreshToken(refresh)
        return Response({
            'access' : str(token.access_token)
        })
    
class ForgotPasswordViewSet(APIView):
    def get(self, request):
        return Response("Forgot password(GET)")
    
    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response({
                "error" : "Phone number is required."
            })

        try:
            user = models.CustomUser.objects.get(phone_number = phone_number)
            models.Verification.objects.filter(user = user).delete()
            otp = random.randint(100000, 999999)
            models.Verification.objects.create(
                user = user,
                otp = otp
            )
            return Response({
                "success" : "OTP sent successfully."
            })

        except models.CustomUser.DoesNotExist:
            return Response({
                "error" : "User does not exist."
            })