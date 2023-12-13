from django.contrib import admin
from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','account_image','gender']
    list_filter = ['user','gender']

admin.site.register(Account,AccountAdmin)

class FavoriteArticleAdmin(admin.ModelAdmin):
    list_display = ['article','user','create_at']
admin.site.register(FavoriteArticle, FavoriteArticleAdmin)