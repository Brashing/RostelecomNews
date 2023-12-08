from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news_index'),
    # path('<int:id>', views.news_detail, name='news_detail'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='news_detail'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='news_delete'),
    path('news_input/', views.news_input, name='news_input'),
    path('news_subscribe/', views.news_subscribe, name='news_subscribe'),
]
