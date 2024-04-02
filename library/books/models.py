from django.db import models


class Book(models.Model):
    author_name = models.CharField(max_length=20)
    book_name = models.CharField(max_length=20)
    price = models.IntegerField()
    cover = models.ImageField(upload_to="books/image")
    pdf = models.FileField(upload_to="books/pdf")
