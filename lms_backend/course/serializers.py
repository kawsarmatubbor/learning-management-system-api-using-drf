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

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = ['id', 'course', 'title', 'description', 'is_active']
        extra_kwargs = {
            'description' : {
                'required' : False
            }
        }

class CourseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseTeacher
        fields = ['id', 'course', 'teacher', 'is_active']

class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseStudent
        fields = ['id', 'course', 'student', 'is_active']