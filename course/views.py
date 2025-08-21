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
        
class ModuleViewSet(APIView):
    permission_classes = [permissions.IsTeacherOrReadOnly]

    def get(self, request):
        modules = models.Module.objects.filter(is_active = True)
        serializer = serializers.ModuleSerializer(modules, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.ModuleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ModelDetailViewSet(APIView):
    permission_classes = [permissions.IsTeacherOrReadOnly]

    def get(self, request, pk):
        try:
            module = models.Module.objects.get(pk = pk)
            serializer = serializers.ModuleSerializer(module)
            return Response(serializer.data)
        
        except models.Module.DoesNotExist:
            return Response({
                "error" : "Module not found."
            })
        
    def put(self, request, pk):
        try:
            module = models.Module.objects.get(pk = pk)
            serializer = serializers.ModuleSerializer(module, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        except models.Module.DoesNotExist:
            return Response({
                "error" : "Module not found."
            })
        
    def delete(self, request, pk):
        try:
            module = models.Module.objects.get(pk = pk)
            module.delete()
            return Response({
                "success" : "Module deleted successfully."
            })
        
        except models.Module.DoesNotExist:
            return Response({
                "error" : "Module not found."
            })
        
class CourseTeacherViewSet(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self, request):
        course_teachers = models.CourseTeacher.objects.filter(is_active = True)
        serializer = serializers.CourseTeacherSerializer(course_teachers, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CourseTeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CourseTeacherDetailViewSet(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            course_teacher = models.CourseTeacher.objects.get(pk = pk)
            serializer = serializers.CourseTeacherSerializer(course_teacher)
            return Response(serializer.data)
        
        except models.CourseTeacher.DoesNotExist:
            return Response({
                "error" : "Course teacher not found."
            })
        
    def put(self, request, pk):
        try:
            course_teacher = models.CourseTeacher.objects.get(pk = pk)
            serializer = serializers.CourseTeacherSerializer(course_teacher, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        except models.CourseTeacher.DoesNotExist:
            return Response({
                "error" : "Course teacher not found."
            })
        
    def delete(self, request, pk):
        try:
            course_teacher = models.CourseTeacher.objects.get(pk = pk)
            course_teacher.delete()
            return Response({
                "success" : "Course teacher deleted successfully."
            })
        
        except models.CourseTeacher.DoesNotExist:
            return Response({
                "error" : "Course teacher not found."
            })
    
class CourseStudentViewSet(APIView):
    permission_classes = [permissions.IsTeacherOrReadOnly]

    def get(self, request):
        course_students = models.CourseStudent.objects.filter(is_active = True)
        serializer = serializers.CourseStudentSerializer(course_students, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CourseStudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CourseStudentDetailViewSet(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            course_student = models.CourseStudent.objects.get(pk = pk)
            serializer = serializers.CourseStudentSerializer(course_student)
            return Response(serializer.data)
        
        except models.CourseStudent.DoesNotExist:
            return Response({
                "error" : "Course student not found."
            })
        
    def put(self, request, pk):
        try:
            course_student = models.CourseStudent.objects.get(pk = pk)
            serializer = serializers.CourseStudentSerializer(course_student, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        except models.CourseStudent.DoesNotExist:
            return Response({
                "error" : "Course student not found."
            })
        
    def delete(self, request, pk):
        try:
            course_student = models.CourseStudent.objects.get(pk = pk)
            course_student.delete()
            return Response({
                "success" : "Course student deleted successfully."
            })
        
        except models.CourseStudent.DoesNotExist:
            return Response({
                "error" : "Course student not found."
            })