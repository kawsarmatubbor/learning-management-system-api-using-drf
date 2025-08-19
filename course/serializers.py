from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'title', 'is_active']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'title', 'description', 'thumbnail', 'price', 'is_active']
        extra_kwargs = {
            'description' : {
                'required' : False,
                'allow_blank' : True
            }
        }