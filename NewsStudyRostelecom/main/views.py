from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def user_profile(request):
    return render(request, 'main/user_profile.html')

def login(request):
    return render(request, 'main/login.html')

def registration(request):
    return render(request, 'main/registration.html')

def custom_404(request, exception):
    return render(request, 'main/custom_404.html')
    #return HttpResponse(f'Ой, какая жалость!:{exception}')