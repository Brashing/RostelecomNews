from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from news.models import Article
from django.core.paginator import Paginator
from django.views.generic import DetailView, DeleteView, UpdateView, ListView
from .models import *
from .forms import *
import datetime

# from ..news.models import Image

@login_required(login_url="/users/login")
def users(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None:
                data_account = form.save(commit=False)
                data_account.user = current_user
                data_account.save()
                form.save_m2m()
                return redirect('user_profile')
    else:
        form = AccountForm()
    context = {
        'form': form,
        'articles': articles,
        # 'page_obj': page_obj,
    }
    return render(request, 'users/users.html',context)

def login(request):
    return render(request, 'users/login.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request,f'{username} зарегистрирован!')
            authenticate(username=username,password=password)
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)
