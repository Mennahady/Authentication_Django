from django.urls import path
from .views import (
    DoctorRegistrationView,
    PatientRegistrationView,
    PasswordResetRequestView,
    PasswordResetConfirmView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/doctor/', DoctorRegistrationView.as_view(), name='doctor_register'),
    path('register/patient/', PatientRegistrationView.as_view(), name='patient_register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password/reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] 