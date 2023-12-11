from django.shortcuts import render
from django.views.generic import ListView
from news.models import Article
from .models import *
from django.http import HttpResponse


def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }

    return render(request, 'main/index.html', context)

def custom_404(request, exception):
    return render(request, 'main/custom_404.html')

