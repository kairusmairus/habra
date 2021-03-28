
from django.contrib import admin
from django.urls import path, include
from core.views import *#imported from views
from django.conf import settings # for static files
from django.conf.urls.static import static
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles, name="articles"),
    
    path('authors/', authors, name='authors'),
    path("about/", about, name="about"),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path("profile/", profile, name="profile"),
    
    path("article/", include("core.urls")), 
    path("library/", include("library.urls")),   # library app

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
