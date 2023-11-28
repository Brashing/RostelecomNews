from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def index(request):
    # articles = Article.published.all()
    # context = {'articles':articles}
    return render(request, 'main/index.html')

def custom_404(request, exception):
    return render(request, 'main/custom_404.html')
    #return HttpResponse(f'Ой, какая жалость!:{exception}')