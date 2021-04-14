from django.urls import path
from . import views


urlpatterns = [
    path("<int:id>/", views.book_detail, name = "book_detail"),
    path("", views.all_books, name = "all_books"),
    path("<int:id>/edit/", views.edit_book, name='edit_book'),
    path('new/', views.add_book, name='add_book'),
    
]