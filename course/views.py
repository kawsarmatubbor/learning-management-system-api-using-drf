from rest_framework.views import APIView
from rest_framework.response import Response
from . import permissions
from . import serializers
from . import models

class CategoriesViewSet(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    
    def get(self, request):
        categories = models.Category.objects.filter(is_active = True)
        serializer = serializers.CategorySerializer(categories, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CategoryDetailViewSet(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            category = models.Category.objects.get(pk = pk)
            serializer = serializers.CategorySerializer(category)
            return Response(serializer.data)
        
        except models.Category.DoesNotExist:
            return Response({
                "error" : "Category not found."
            })
        
    def put(self, request, pk):
        try:
            category = models.Category.objects.get(pk = pk)
            serializer = serializers.CategorySerializer(category, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        except models.Category.DoesNotExist:
            return Response({
                "error" : "Category not found."
            })
        
    def delete(self, request, pk):
        try:
            category = models.Category.objects.get(pk = pk)
            category.delete()
            return Response({
                "success" : "Category deleted successfully."
            })
        
        except models.Category.DoesNotExist:
            return Response({
                "error" : "Category not found."
            })
        
class CourseViewSet(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self, request):
        courses = models.Course.objects.filter(is_active = True)
        serializer = serializers.CourseSerializer(courses, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CourseDetailViewSet(APIView):
    def get(self, request, pk):
        try:
            course = models.Course.objects.get(pk = pk)
            serializer = serializers.CourseSerializer(course)
            return Response(serializer.data)
        
        except models.Course.DoesNotExist:
            return Response({
                "error" : "Course not found."
            })
        
    def put(self, request, pk):
        try:
            course = models.Course.objects.get(pk = pk)
            serializer = serializers.CourseSerializer(course, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        except models.Course.DoesNotExist:
            return Response({
                "error" : "Course not found."
            })
        
    def delete(self, request, pk):
        try:
            course = models.Course.objects.get(pk = pk)
            course.delete()
            return Response({
                "success" : "Course deleted successfully."
            })
        
        except models.Course.DoesNotExist:
            return Response({
                "error" : "Course not found."
            })