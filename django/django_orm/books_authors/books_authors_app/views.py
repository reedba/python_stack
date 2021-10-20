from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        'books':Book.objects.all(),
        'authors':Author.objects.all()

    }
    return render(request,'index.html',context)

def create_book(request):
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
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect('view_book')


def author_list(request):
    context = {
        'authors':Author.objects.all()
    }
    return render(request, 'add_author.html',context)

def create_author(request):
    if request.method == 'POST':
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/author_list')

def view_author(request, author_id):
    context = {
        'author':Author.objects.get(id = author_id),
        'books':Book.objects.all(),
        'authors':Author.objects.all()
    }
    print(context['author'].id)
    return render(request,'author_details.html',context)

def delete_author(request, author_id):
    author = Author.objects.get(id = author_id)
    author.delete()
    return redirect('/author_list')

def delete_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return redirect('/')

def add_author(request,book_id):
    this_author = Author.objects.get(id = request.POST['author_selected'])
    this_book = Book.objects.get(id = book_id)
    this_book.authors.add(this_author)
    return redirect(f'/view_book/{book_id}')


def add_book(request,author_id):
    this_author = Author.objects.get(id = author_id)
    this_book = Book.objects.get(id = request.POST['author_selected'])
    this_author.books.add(this_book)
    return redirect(f'/view_book/{author_id}')



