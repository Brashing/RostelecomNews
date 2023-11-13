from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def custom_404(request, exception):
    # return render(request, 'main/sidebar.html')
    return HttpResponse(f'Ой, какая жалость!:{exception}')