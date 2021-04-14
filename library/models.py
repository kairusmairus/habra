from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Author(models.Model):
#     name = models.TextField()
#     birth_date = models.DateField()
#     death_date = models.DateField()
#     birth_place = models.TextField()

class Book(models.Model):
    author = models.CharField(max_length=100, default = 'uknown', verbose_name="Автор")
    title = models.CharField(max_length=250, verbose_name="Название")
    written_date = models.DateField()
    pages_num = models.IntegerField()
    content = models.TextField()
    #writer = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=100, default = 'Русский') 
    added_by = models.ForeignKey( to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Добавил") 

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"     

    def __str__(self):
        return self.title 
