from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from . import models

class RegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    password_2 = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    class Meta:
        model = models.CustomUser
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'password_1', 'password_2']
        extra_kwargs = {
            'first_name' : {'required' : True},
            'last_name' : {'required' : True},
        }

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError("Passwords don't match.")
        return attrs
    
    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(
            phone_number = validated_data['phone_number'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password_1']
        )
        return user