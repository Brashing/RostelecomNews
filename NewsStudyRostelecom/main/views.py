from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def news_1(request):
    return render(request, 'main/news_1.html')

def news_2(request):
    return render(request, 'main/news_2.html')

def news_3(request):
    return render(request, 'main/news_3.html')

def news_4(request):
    return render(request, 'main/news_4.html')

def news_5(request):
    return render(request, 'main/news_5.html')

def news_6(request):
    return render(request, 'main/news_6.html')

def user_profile(request):
    return render(request, 'main/user_profile.html')

def custom_404(request, exception):
    return render(request, 'main/custom_404.html')
    #return HttpResponse(f'Ой, какая жалость!:{exception}')