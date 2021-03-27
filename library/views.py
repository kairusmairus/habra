from django.shortcuts import render
from library.models import Book
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



# def book_detail(request, pk):
    
#     book_objs = Book.objects.filter(id=pk) #когда было pk=id не работало
#     context = {
#         "libitems" : book_objs,
#         # "authors" : author_obj,
#     }

#     return render(request, "library/book_detail.html", context)

 

# def post_new(request):
#     form = PostForm()
#     return render(request, 'library/post_new.html', {'form': form})
