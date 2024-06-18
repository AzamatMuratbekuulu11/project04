from tkinter import CASCADE
from django.db import models
from django.db.models import ForeignKey


class Author(models.Model):
    # author_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    birth_date = models.DateField()

    def __str__(self):
        return self.last_name

class Book(models.Model):
    title_name = models.CharField(max_length=32)
    author = models.ForeignKey#(Author, on_delete=models,CASCADE)
    published_date = models.DateField()
    pages = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    have = models.BooleanField(default=True)

    def __str__(self):
        return self.title_name

