from django.shortcuts import render
from news.models import Article
from .models import *
from django.http import HttpResponse

# from ..news.models import Image


def index(request):
    articles = Article.objects.all()
    # images = Image.objects.all()
    # articles = Article.published.all()
    context = {
        'articles':articles,
        # 'images': images
    }
    return render(request, 'main/index.html', context)

def custom_404(request, exception):
    return render(request, 'main/custom_404.html')
    #return HttpResponse(f'Ой, какая жалость!:{exception}')