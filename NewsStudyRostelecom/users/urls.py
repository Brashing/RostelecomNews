from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.users, name='user_profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('password', views.password_update, name='password'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('favorites/<int:id>', views.add_to_favorites, name='favorites'),
    # path('favorites_list', views.FavoritesListView.as_view(), name='favorites_list'),
    path('contact_page', views.contact_page, name='contact_page'),
]