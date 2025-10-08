from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),
    path('verification/', views.verification_view, name='verification'),
    path('password-reset/', views.password_reset_view, name='password-reset'),
]