from django.contrib import admin
from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','account_image','gender']
    list_filter = ['user','gender']

admin.site.register(Account,AccountAdmin)

class FavoriteArticleAdmin(admin.ModelAdmin):
    ordering = ['user','-create_at','article']
    list_display = ['user','article','create_at']
    list_filter = ['user','article','create_at']

admin.site.register(FavoriteArticle, FavoriteArticleAdmin)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['status','name', 'email']
    list_filter = ['status','name', 'email']
    list_display_links = ['name']
    # list_editable = ['status']