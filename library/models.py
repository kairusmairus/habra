from django.db import models

# Create your models here.

# class Author(models.Model):
#     name = models.TextField()
#     birth_date = models.DateField()
#     death_date = models.DateField()
#     birth_place = models.TextField()

class Book(models.Model):
    author = models.CharField(max_length=100, default = 'Неизвестно')
    title = models.TextField()
    written_date = models.DateField()
    pages_num = models.IntegerField()
    content = models.TextField()
    #writer = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=100, default = 'Русский')    
