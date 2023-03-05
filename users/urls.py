"""Defines URL patters for users."""

from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('choose-registration-type/', views.choose_registration_type, name='choose_registration_type'),
    path('register-individual/', views.register_individual, name='register_individual'),
    path('register-legal-entity/', views.register_legal_entity, name='register_legal_entity'),
    path('login-with-username/', views.login_with_username, name='login_with_username'),
    path('login-with-phone-number', views.login_with_phone_number, name='login_with_phone_number'),
]
