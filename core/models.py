from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField(blank=True, null=True)
    
    author = models.ForeignKey(
        to="Author",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="article",
        verbose_name="Автор"
    )

    readers = models.ManyToManyField(
        to=User,
        related_name="readed_articles",
        blank=True,
    )
    views = models.IntegerField(default=0, verbose_name="Просмотры: ")
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    picture = models.ImageField(
        upload_to="images/",
        null=True, blank=True,
        verbose_name="Картинка статьи"    
    )
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(
        to=User,
        related_name="author",
        verbose_name="Пользователь",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    nik = models.CharField(max_length=55)

    photo = models.ImageField(upload_to="photo", null=True, blank=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


    
    def __str__(self):
        return self.nik        