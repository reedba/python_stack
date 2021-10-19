from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        'books':Book.objects.all(),
        'authors':Author.objects.all()

    }
    return render(request,'index.html',context)

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect('/')

def view_book(request,book_id):
    context = {
        'book':Book.objects.get(id = book_id),
        'books':Book.objects.all(),
        'authors':Author.objects.all()
    }
    return render(request,'book_details.html',context)

def book_details(request):
    Book.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect('book_details.html')


def author_list(request):
    context = {
        'authors':Author.objects.all(),
    }
    return render(request, 'add_author.html',context)

def add_author(request):
    if request.method == 'POST':
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('add_author.html')

def view_author(request, author_id):
    context = {
        'author':Author.objects.get(id = author_id),
        'books':Book.objects.all(),
        'authors':Author.objects.all()
    }
    return render(request,'author_details.html',context)



