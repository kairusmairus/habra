# Generated by Django 3.1.7 on 2021-04-15 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_article_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='header_image',
        ),
    ]
