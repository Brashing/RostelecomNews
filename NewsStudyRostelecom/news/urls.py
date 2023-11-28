from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news_index'),
    path('<int:id>', views.news_detail, name='news_detail'),
    path('news_input/', views.news_input, name='news_input'),
]
