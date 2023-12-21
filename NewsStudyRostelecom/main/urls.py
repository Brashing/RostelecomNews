from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('', views.about, name='about'),
]
