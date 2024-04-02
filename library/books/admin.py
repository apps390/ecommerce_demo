from django.contrib import admin
from books.models import Book
from django.http import HttResponse

# Register your models here.
admin.site.register(Book)