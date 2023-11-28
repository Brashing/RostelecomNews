from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def users(request):
    users = Account.objects.all()
    context = {'users' : users}
    # print(request.user,request.user.id)
    # user_acc = Account.objects.get(user=request.user)
    # print(Account.objects.get(user=request.user).birthdate,user_acc.gender)
    return render(request, 'users/users.html',context)
    # return HttpResponse(f'Ой, какая жалость!:{exception}')

def login(request):
    return render(request, 'users/login.html')

def registration(request):
    return render(request, 'users/registration.html')
