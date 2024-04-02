from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from books.forms import Bookform
from django.contrib.auth.decorators import login_required

def addbook(request):
    book_details = {'authors': [{'name': 'william shakesphere', 'book': 'macbeth', 'year': 1698},
                                {'name': 'subhash chandran', 'book': 'samudrashila', 'year': 2008}
                                ]}
    return render(request, "home.html", book_details)

@login_required
def addlibrary(request):
    b = Book.objects.all()
    return render(request, "library.html", {'book': b})

@login_required
def add_author(request):
    return HttpResponse("<h1>welcome to bombay </h1>")

@login_required
def add_books(request):
    if request.method == "POST":
        A = request.POST['Author']
        T = request.POST['Book']
        P = request.POST['Price']
        I = request.FILES['Cover']
        F = request.FILES['pdf']
        b = Book.objects.create(author_name=A, book_name=T, price=P, cover=I, pdf=F)
        b.save()
        return addlibrary(request)
    return render(request, 'addbook.html')


def edit(request, n):
    p = Book.objects.get(id=n)
    return render(request, 'edit.html', {'p': p})



def delete(request, d):
    p = Book.objects.get(id=d)
    p.delete()
    return addlibrary(request)


def view(request, v):
    k = Book.objects.get(id=v)
    return render(request, 'view.html', {'k': k})


def add_novels(request):
    if (request.method == "POST"):
        form = Bookform(request.POST)
        if form.is_valid():
            form.save()
            return addlibrary(request)

    form = Bookform()
    return render(request, 'addnovel.html', {'form': form})
