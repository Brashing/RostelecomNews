from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.users, name='user_profile'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]