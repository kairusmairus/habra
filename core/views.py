from django.shortcuts import render, HttpResponse, redirect
from .models import * #импорт из моделей чтобы он знал откуда Article
from django.contrib.auth.models import User
from .forms import PostArtForm
from django.db.models import Q
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

# Create your views here.
def articles(request):
    articles = Article.objects.all() # 
    return render(
        request, "articles.html", {"articles":  articles})
    #"article" то как называется в html, article название обхекта  
    # 
def authors(request):
    authors = Author.objects.all()
    return render(
        request, "authors.html", {"authors": authors })

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    return render(
        request, "article.html", {"article": article })  

def about(request):
    return render(request, "about.html")  

def profile(request):
    user = User.objects.all()
    
    return render(
         request, "profile.html", {"profile":user})    

def edit_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render(request, "update.html", {"article":article})

def add_art(request):
    if request.method == "POST":
        form = PostArtForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.save()
            return redirect(article_page, post.pk)
    else:
        form = PostArtForm()
    return render(request, 'add_art.html', {'form': form})    


def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect(articles)#return HttpResponse("Ваша запись удалена...") #may do redirect also
    
def hide_article(request, id):
    article = Article.objects.get(id=id)
    article.is_active = False
    article.save()
    return redirect(articles) #render(request, "articles.html", {"articles":articles}) 


def search(request):
    word = request.GET.get("searchword") 
    articles = Article.objects.filter(
        Q(title__icontains = word) | Q(text__icontains = word), is_active = True)   
    return render(request, "articles.html", {"articles" : articles})    

def author_page(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, "author.html", {"author" : author})    