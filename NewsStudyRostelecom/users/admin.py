from django.contrib import admin
from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','account_image','gender']
    list_filter = ['user','gender']

admin.site.register(Account,AccountAdmin)

class FavoriteArticleAdmin(admin.ModelAdmin):
    ordering = ['-create_at','user','article']
    list_display = ['user','article','create_at']
    list_filter = ['user','article','create_at']

admin.site.register(FavoriteArticle, FavoriteArticleAdmin)