from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
import random

@api_view(["POST"])
def registration_view(request):
    serializer = serializers.RegistrationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({
        "message" : "This is a protected view."
    })

@api_view(["POST"])
def forgot_password_view(request):
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
            "error" : "User does not exist.",
            "phone_number" : phone_number
        })
    
    except models.Verification.DoesNotExist:
        return Response({
            "error" : "Request again for OTP."
        })
    
@api_view(["POST"])
def verification_view(request):
    phone_number = request.data.get('phone_number')
    up_otp = request.data.get('otp')
    
    if not phone_number:
        return Response({
            "error" : "Phone number is required."
        })
    
    if not up_otp:
        return Response({
            "error" : "OTP is required."
        })

    try:
        user = models.CustomUser.objects.get(phone_number = phone_number)
        db_otp = models.Verification.objects.get(user = user.id)

        if str(up_otp) == str(db_otp.otp):
            db_otp.delete()
            return Response({
                "success" : "Verification success.",
                "phone_number" : phone_number
            })
        return Response({
            "error" : "Invalid OTP."
        })
        
    except models.Verification.DoesNotExist:
        return Response({
            "error" : "OTP not found."
        })
    
@api_view(['POST'])
def password_reset_view(request):
    serializer = serializers.PasswordResetSerializer(data = request.data)

    if serializer.is_valid():
        phone_number = serializer.validated_data.get('phone_number')
        password_1 = serializer.validated_data.get('password_1')

        try:
            user = models.CustomUser.objects.get(phone_number = phone_number)
            user.set_password(password_1)
            user.save()
            return Response({
                "success" : "Password reset successful."
            })
        except models.CustomUser.DoesNotExist:
            return Response({
                "error" : "User does not exist."
            })
        
    return Response(serializer.errors)