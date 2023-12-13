import json

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

def search_auto(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        q = request.GET.get('term','')
        articles = Article.objects.filter(title__icontains=q)
        results =[]
        for a in articles:
            results.append(a.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def custom_404(request, exception):
    return render(request, 'main/custom_404.html')

