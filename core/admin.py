from django.contrib import admin
from .models import Article, Author
from library.models import Book

# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Book)