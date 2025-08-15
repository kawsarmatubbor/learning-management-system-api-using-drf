from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

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