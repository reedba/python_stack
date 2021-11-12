from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

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
    return redirect('/wishes')


def login(request):
    if request.method == 'POST':
        errors = User.objects.Login_Validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/')
        request.session['user_id'] = User.objects.filter(email = request.POST['log_email'])[0].id
    return redirect ('/wishes')

def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    return render(request, 'index.html')


def wishes(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        'user': this_user[0],
        'wishes': Wishes.objects.all(),
        'users':User.objects.all(),
        'user_session':User.objects.filter(id = request.session['user_id'])
    }
    return render(request, 'wishes.html', context)


def remove_wish(request, id):
    wish = Wishes.objects.get(id = id)
    wish.delete()
    return redirect('/wishes')

def granted(request,id):
    user = User.objects.get(id=request.session["user_id"])
    wish = Wishes.objects.get(id=id)
    user.wishes_granted.add(wish)
    wish.save()
    return redirect('/wishes')


def create_wish(request):
    context = {
        'user':User.objects.get(id = request.session['user_id'])
    }
    return render(request,'create_wish.html', context)

def add_wish(request):
    if request.method == 'POST':
        errors = Wishes.objects.Wish_Validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/create_wish')
    wish = Wishes.objects.create( item = request.POST['item'],description = request.POST['description'], poster = User.objects.get(id = request.session['user_id']))
    return redirect('/create_wish')

def edit(request, id):
    wish = Wishes.objects.get(id=id)
    context = {
        'wish':wish
    }
    return render(request,'edit.html', context)


def update_wish(request, id):
    if request.method == 'POST':
        errors = Wishes.objects.Wish_Validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/create_wish')
    edit_wish = Wishes.objects.get(id=id)

    edit_wish.item = request.POST['item']
    edit_wish.description = request.POST['description']
    edit_wish.save()
    return redirect('/wishes')

def cancel(request):
    return redirect('/wishes')