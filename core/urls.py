from django.urls import path
from . import views
from django.conf import settings # for static files
from django.conf.urls.static import static

#app_name = 'core'  --if add this all crashes - WHY???

urlpatterns = [
    path("<int:id>/", views.article_page, name="article"),
    path("<int:pk>/edit/", views.edit_article, name='article-edit'),
    
    path("<int:id>/delete", views.delete_article, name='article-delete'),
    path("<int:id>/hide", views.hide_article, name='article-hide'),
    path("add/", views.add_art, name="art-add"),
    path('search/', views.search, name="search"),
]