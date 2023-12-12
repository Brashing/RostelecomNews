from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
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
        form = AccountUpdateForm(request.POST)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None:
                data_account = form.save(commit=False)
                data_account.user = current_user
                data_account.save()
                form.save_m2m()
                # for img in request.FILES.getlist('image_field'):
                #     Image.objects.create(account=data_account, image=img, title=img.name)
                return redirect('user_profile')
    else:
        form = AccountUpdateForm()
    context = {
        'form': form,
        'articles': articles,
    }
    return render(request, 'users/users.html',context)

def login(request):
    return render(request, 'users/login.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Персонал')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request,f'{username} зарегистрирован!')
            authenticate(username=username,password=password)
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

def profile_update(request):
    user = request.user
    account = Account.objects.get(user=user)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=account)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            messages.success(request,"Профиль успешно обновлен")
            return redirect('profile')
        else:
            pass
    else:
        context = {'account_form':AccountUpdateForm(instance=account),
                   'user_form':UserUpdateForm(instance=user)}
    return render(request,'users/edit_profile.html',context)

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
def password_update(request):
    user = request.user
    form = PasswordChangeForm(user,request.POST)
    if request.method == 'POST':
        if form.is_valid():
            password_info = form.save()
            update_session_auth_hash(request,password_info)
            messages.success(request,'Пароль успешно изменен')
            return redirect('user_profile')

    context = {"form": form}
    return render(request,'users/edit_password.html',context)