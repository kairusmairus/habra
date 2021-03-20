from django.shortcuts import render, HttpResponse
from .models import * #импорт из моделей чтобы он знал откуда Article
# Create your views here.
def articles(request):
    articles = Article.objects.all() # 
    return render(
        request, "articles.html", {"articles":articles})
    #"article" то как называется в html, article название обхекта  
    # 
def authors(request):
    authors = Author.objects.all()
    return render(
        request, "authors.html", {"authors": authors })

def article(request, id):
    articles = Articles.objects.get(id=id)
    return render(
        request, "article.html", {"article": article })  

def about(request):
    return render(request, "about.html")          