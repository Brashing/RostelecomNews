from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','source','categories','author','date']
    list_filter = ['title','author','date','categories','source']

class TagAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['title','status']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)