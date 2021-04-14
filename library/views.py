from django.shortcuts import render, redirect
from .models import Book
from .forms import PostForm

# Create your views here.

def all_books(request):
    
    # select * from books вбырать все из books и name из authors
   books = Book.objects.all()
   #('SELECT library_author.id, library_book.title, library_book.written_date, library_book.pages_num, library_book.language from library_book inner join library_author on library_book.id=library_author.id')
   context={
       "booklist":books,
   }
   return render(request, "library/books.html", context)   



def book_detail(request, id):
    
    books = Book.objects.filter(id=id) #когда было pk=id не работало
    context = {
        "books" : books,
        # "authors" : author_obj,
    }

    return render(request, "library/book_detail.html", context)

 

def add_book(request):
    if request.method == "GET":
        return render(request, "library/addbook.html")
    elif request.method == "POST":
        form = request.POST
        author = form.get("author")
        title = form.get("title")
        content = form.get("content")
        pages = form.get("pages")
        date = form.get("date")

        new_book = Book()
        new_book.title = title
        new_book.content= content
        user = request.user
        new_book.added_by = user
        new_book.author = author
        new_book.pages_num = pages
        new_book.written_date = date
       
        new_book.save()
        return redirect(book_detail, new_book.pk)
    
def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        book.author = request.POST.get("author")
        book.content = request.POST.get("content")
        book.title = request.POST.get("title")
        book.pages = request.POST.get("pages")
        book.date = request.POST.get("date")
        book.save()
        return redirect(book_detail, id)
    return render(request, "library/edit_book.html", {"book":book})

