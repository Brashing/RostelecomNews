from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news_index'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('article_list/', views.ArticleListView.as_view(), name='search_news'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='news_detail'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='news_delete'),
    path('news_input/', views.news_input, name='news_input'),
    path('news_request/', views.news_request, name='news_request'),
    path('news_subscribe/', views.news_subscribe, name='news_subscribe'),
]
