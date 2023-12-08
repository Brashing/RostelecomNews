from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView, ListView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import datetime

class ArticleDetailView(DetailView):
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
    template_name = 'news/news_input.html'
    fields = ['categories','title','anouncement','text','source','sourcename','tags']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news_index')
    template_name = 'news/news_delete.html'


def news(request):
    news = Article.objects.all()
    paginator = Paginator(news,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    a = news.first()
    categories = a.categories

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
    context = {
        'news': news,
        'author_list': author_list,
        'selected': selected,
        'categories': categories,
        'page_obj': page_obj,
    }
    return render(request, 'news/news.html', context)

@login_required(login_url="/")
def news_input(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None:
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.date = datetime.date.today()
                new_article.save()
                # form = ArticleForm()
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
            return redirect('news_index')
    else:
        form = SubscribeForm()
    return render(request,'news/news_subscribe.html', {'form': form})

