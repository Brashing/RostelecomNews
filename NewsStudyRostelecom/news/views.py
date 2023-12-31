from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView, ListView
from .utils import ViewCountMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import datetime
import json
from users.models import FavoriteArticle
from django.db.models import Count


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


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search_input')
        articles = Article.objects.filter(title__icontains=query)
        return articles

class ArticleDetailView(ViewCountMixin, DetailView):
    model = Article
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object = self.object
        images = Image.objects.filter(article=current_object)
        context['images'] = images
        return context

class ArticleUpdateView(UpdateView):
    model = Article
    success_url = reverse_lazy('user_profile')
    template_name = 'news/news_input.html'
    fields = ['categories','title','anouncement','text','source','sourcename','tags']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('user_profile')
    template_name = 'news/news_delete.html'

@login_required(login_url="/")
def news_input(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.is_staff == True:
                if current_user.id != None:
                    new_article = form.save(commit=False)
                    new_article.author = current_user
                    new_article.date = datetime.date.today()
                    new_article.status = True
                    new_article.save()
                    form.save_m2m()
                    for img in request.FILES.getlist('image_field'):
                        Image.objects.create(article=new_article, image=img, title=img.name)
                    return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request, 'news/news_input.html', {'form': form})

def news_subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Ваш запрос на рассылку новостей успешно отправлен!')
            return redirect('home')
    else:
        form = SubscribeForm()
    return render(request,'news/news_subscribe.html', {'form': form})

def news(request):
    favorite_article = FavoriteArticle.objects.filter(user=request.user)
    categories = Article.categories_list
    author_list = User.objects.filter(article__isnull=False).filter(article__status=True).distinct()
    if request.method == "POST":
        selected_author = int(request.POST.get('author_filter'))
        selected_category = int(request.POST.get('category_filter'))
        request.session['author_filter'] = selected_author
        request.session['category_filter'] = selected_category
        if selected_author == 0:
            articles = Article.published.all()
        else:
            articles = Article.published.filter(author=selected_author)
        if selected_category != 0:
            articles = articles.filter(categories__icontains=categories[selected_category-1][0])
    else:
        value = request.session.get('search_input')
        if value != None:
            articles = Article.published.filter(title__icontains=value)
        else:
            selected_author = request.session.get('author_filter')
            selected_category = request.session.get('category_filter')
            articles = Article.published.all()
            if selected_author != None and int(selected_author) != 0:
                articles = articles.filter(author=selected_author)
            else:
                selected_author = 0
            if selected_category != None and int(selected_category) != 0:
                articles = articles.filter(categories__icontains=categories[selected_category - 1][0])
            else:
                selected_category = 0
    articles = articles.order_by('-date')
    total = len(articles)
    p = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {
        'articles': page_obj,
        'author_list': author_list,
        'selected_author': selected_author,
        'total': total,
        'categories': categories,
        'selected_category': selected_category,
        'favorite_article': favorite_article,
    }
    return render(request, 'news/news.html', context)


@login_required(login_url="/")
def news_request(request):
    if request.method == 'POST':
        form = ArticleRequestForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.is_staff == False:
                if current_user.id != None:
                    new_article = form.save(commit=False)
                    new_article.author = current_user
                    new_article.date = datetime.date.today()
                    new_article.save()
                    form.save_m2m()
                    for img in request.FILES.getlist('image_field'):
                        Image.objects.create(article=new_article, image=img, title=img.name)
                    return redirect('news_index')
    else:
        form = ArticleRequestForm()
    return render(request, 'news/news_request.html', {'form': form})