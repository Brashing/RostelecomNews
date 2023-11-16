from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('news_1/', views.news_1, name='news_1'),
    path('news_2/', views.news_2, name='news_2'),
    path('news_3/', views.news_3, name='news_3'),
    path('news_4/', views.news_4, name='news_4'),
    path('news_5/', views.news_5, name='news_5'),
    path('news_6/', views.news_6, name='news_6'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('news_input/', views.news_input, name='news_input'),
]
