from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationViewSet.as_view(), name='registration'),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('protected/', views.protected_view, name='protected'),
    path('refresh/', views.RefreshView.as_view(), name='refresh'),
    path('forgot-password/', views.ForgotPasswordViewSet.as_view(), name='forgot-password'),
]