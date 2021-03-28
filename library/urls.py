from django.urls import path
from . import views


urlpatterns = [
    path("<int:pk>/", views.book_detail, name = "book_detail"),
    path("", views.all_books, name = "all_books"),
    path('new/', views.post_new, name='post_new'),
]