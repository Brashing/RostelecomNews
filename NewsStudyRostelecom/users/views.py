import json

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from .forms import *

from django.contrib.auth.decorators import login_required
from news.models import Article
@login_required
def add_to_favorites(request, id):
    article = Article.objects.get(id=id)
    bookmark = FavoriteArticle.objects.filter(user=request.user.id,
                                              article=article)
    if bookmark.exists():
        bookmark.delete()
        messages.warning(request,f"Новость '{article.title}' удалена из избранного")
    else:
        bookmark = FavoriteArticle.objects.create(user=request.user, article=article)
        messages.success(request,f"Новость '{article.title}' добавлена в избранное")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url="/users/login")
def users(request):
    author = User.objects.get(id=request.user.id)
    articles = Article.objects.filter(author=author)
    if request.method == "POST":
        articles = articles.filter(author=author)
    total = len(articles)
    p = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {
        'articles': page_obj,
        'total': total,
    }
    return render(request, 'users/users.html',context)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Персонал')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            Account.objects.create(user=user, nickname=user.username)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'{username} зарегистрирован! Заполните данные своего аккаунта.')
            return redirect('profile_update')
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
            messages.success(request,"Профиль успешно обновлен!")
            return redirect('news_index')
        else:
            pass
    else:
        context = {'account_form':AccountUpdateForm(instance=account),
                   'user_form':UserUpdateForm(instance=user),
                   }
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

# def contact_page(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print('Сообщение отправлено', form.cleaned_data)
#         else:
#             print(form.errors)
#     else:
#         form = ContactForm()
#     context = {'form': form}
#     return render(request, 'users/contact_page.html', context)

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено разработчикам сайта! Благодарим Вас за обратную связь!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'users/contact_page.html', {'form': form})