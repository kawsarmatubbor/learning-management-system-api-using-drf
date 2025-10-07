from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesViewSet.as_view(), name='categories'),
    path('categories/<str:slug>/', views.CategoryDetailViewSet.as_view(), name='category-detail'),
    path('categories/<str:slug>/courses/', views.category_courses_view, name='category-courses'),
    path('courses/', views.CourseViewSet.as_view(), name='courses'),
    path('courses/<str:slug>/', views.CourseDetailViewSet.as_view(), name='courses-detail'),
    path('courses/<str:slug>/modules/', views.CourseModulesViewSet.as_view(), name='courses-modules'),
    path('courses/<str:slug>/teachers/', views.CourseTeachersViewSet.as_view(), name='courses-teachers'),
]
