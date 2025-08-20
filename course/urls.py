from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesViewSet.as_view(), name='categories'),
    path('categories/<int:pk>/', views.CategoryDetailViewSet.as_view(), name='category-detail'),
    path('courses/', views.CourseViewSet.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetailViewSet.as_view(), name='courses-detail'),
    path('modules/', views.ModuleViewSet.as_view(), name='modules'),
    path('modules/<int:pk>/', views.ModelDetailViewSet.as_view(), name='modules-detail'),
]
