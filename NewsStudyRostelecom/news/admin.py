from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['categories','title','author','date']
    list_filter = ['title','author','date','categories']

admin.site.register(Article,ArticleAdmin)