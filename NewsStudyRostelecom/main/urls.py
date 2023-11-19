from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]
