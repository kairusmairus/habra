from django.urls import path
from . import views


urlpatterns = [
    path("<int:id>/", views.article_page, name="article"),
    path("<int:pk>/edit/", views.edit_article, name='article-edit'),
    path("add/", views.add_article, name="article-add"),
    path("<int:id>/delete", views.delete_article, name='article-delete'),
    path("<int:id>/hide", views.hide_article, name='article-hide'),
    
]