from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def register(request):
    if request.method == 'POST':
        errors = User.objects.Validate_Registration(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        #hash the password
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        #create a user
        new_user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email =    request.POST['email'], password = hashed_pw)
        #create a session
        request.session['user_id'] = new_user.id
        return redirect('/')
    return redirect('/all_books')

def all_books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'book': Books.objects.all(),
        'this_user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'all_books.html', context)

def login(request):
    if request.method == 'POST':
        errors = User.objects.Login_Validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/')
        request.session['user_id'] = User.objects.filter(email = request.POST['log_email'])[0].id
    return redirect ('/all_books')

def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    return render(request, 'index.html')

def all_books(request):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context = {
        'all_books':Books.objects.all(),
        'this_user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'all_books.html', context)

def add_book(request):
    errors = Books.objects.book_validator(request.POST)
    current_user = User.objects.get(id=request.session["user_id"])
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/all_books')
    else:
        book = Books.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            creator = current_user)
        # bonus: the book creator automatically favorites the book
        current_user.favorited_books.add(book)
        return redirect('/all_books')

def book_dets(request):
    return render(request, 'book_dets.html')

def edit_book(request):
    return render(request, 'edit_book.html')

