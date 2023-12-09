from django.shortcuts import render
from django.views.generic import ListView
from news.models import Article
from .models import *
from django.http import HttpResponse


def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }

    return render(request, 'main/index.html', context)

# class Search(ListView):
#     news = Article.objects.all()
#     template_name = 'main/search.html'
#     context_object_name = 'news'
#     def get_queryset(self):
#         return Article.objects.filter(title__icontains=self.request.GET.get("q"))
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         # context["q"] = self.request.GET.get("q")
#         return context

def custom_404(request, exception):
    return render(request, 'main/custom_404.html')

