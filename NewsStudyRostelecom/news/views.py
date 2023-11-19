from django.shortcuts import render
from .models import *

def news(request):
    return render(request, 'news/news.html')

def news_input(request):
    return render(request, 'news/news_input.html')

def news_1(request):
    return render(request, 'news/news_1.html')

def news_2(request):
    return render(request, 'news/news_2.html')

def news_3(request):
    return render(request, 'news/news_3.html')

def news_4(request):
    return render(request, 'news/news_4.html')

def news_5(request):
    return render(request, 'news/news_5.html')

def news_6(request):
    return render(request, 'news/news_6.html')

# def index(request):
#     article = Article.objects.all().first()
#     context = {'article':article}
#     return render(request,'news/index.html',context)

# def detail(request,id):
#     article = Article.objects.filter(id=id).first()
#     print(article,type(article))
#     return HttpResponse(f'<h1>{article.title}</h1>')