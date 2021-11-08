from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt  

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.validate_registration(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash,)

    request.session['user_id']= user.id #logs them in
    return redirect('/welcome')


def login(request):
    if request.method == 'POST':
        errors = User.objects.Login_Validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    request.session['user_id']= User.objects.filter(email = request.POST['log_email'])[0].id
    print(request.session['user_id'])
    return redirect('/welcome')


def logout(request):
    request.session.flush()
    return redirect('/')

def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        'user': this_user[0],
        'quotes':Quote.objects.all()
    }

    return render(request, 'welcome.html', context)

def create_quote(request):
    if request.method == 'POST':
        errors = Quote.objects.Quote_Validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/welcome')
    quote = Quote.objects.create(quote = request.POST['quote'],author = request.POST['author'], poster = User.objects.get(id = request.session['user_id']))
    return redirect('/welcome')

def add_like(request, id):
    liked_message = Quote.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/welcome')

def poster_list(request, id):
    context = {
        'user':User.objects.get(id=id)
    }
    return render(request, 'poster_dets.html', context)

def delete_quote(request, id):
        destroyed = Quote.objects.get(id=id)
        destroyed.delete()
        return redirect('/welcome')

def edit_account(request, id):
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        'user': this_user[0],
        'quotes':Quote.objects.all()
    }
    return render(request, 'edit_account.html')

def update(request):
    context = {
        'to_update':User.objects.get(id = request.session['user_id'])
    }
    to_update = User.objects.get(id = request.session['user_id'])

    to_update.first_name = request.POST['update_first_name']
    to_update.last_name = request.POST['update_last_name']
    to_update.email = request.POST['update_email']
    to_update.save()

    return redirect('/edit_account')
