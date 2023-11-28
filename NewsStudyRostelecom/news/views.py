from django.shortcuts import render, HttpResponse

from .models import *
from .forms import *

# from django.db import connection, reset_queries
from django.db.models import Count, Avg, Max, Min


def news(request):
    # all_news = Article.objects.all().values('author','title')
    # for a in all_news:
    #     print(a['author'], a['title'])
    # print(all_news)
    # print(connection.queries)

    # max_article_count_user = User.objects.annotate(Count('article', distinct=True)).order_by('-article__count').first()
    # count_articles = User.objects.annotate(Count('article', distinct=True)).aggregate(Max('article__count'))
    # print(max_article_count_user, count_articles)

    author_list = User.objects.all()
    selected = 0
    if request.method == "POST":
        selected = int(request.POST.get('author_filter'))
        if selected == 0:
            news = Article.objects.all().order_by('-date')
        else:
            news = Article.objects.filter(author=selected).order_by('-date')
    else:
        news = Article.objects.all().order_by('-date')
    context = {'news': news, 'author_list': author_list, 'selected': selected}
    return render(request, 'news/news.html', context)

def news_detail(request, id):
    news = Article.objects.get(id=id)
    # print('Автор новости',':',news.author.account.nickname)
    context = {'news': news}
    return render(request, 'news/news_detail.html', context)


def news_input(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None: #проверили что не аноним
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.save() #сохраняем в БД
                form.save_m2m()
                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request, 'news/news_input.html', {'form': form})

# def index(request):
#     article = Article.objects.all().first()
#     context = {'article':article}
#     return render(request,'news/index.html',context)

# def detail(request,id):
#     article = Article.objects.filter(id=id).first()
#     print(article,type(article))
#     return HttpResponse(f'<h1>{article.title}</h1>')
