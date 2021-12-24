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
    return redirect('/all_tasks')


def login(request):
    if request.method == 'POST':
        errors = User.objects.Login_Validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/')
        request.session['user_id'] = User.objects.filter(email = request.POST['log_email'])[0].id
    return redirect ('/all_tasks')

def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    return render(request, 'index.html')

def create_task(request):
    context = {
        'this_user':User.objects.get(id = request.session['user_id']),
        'users': User.objects.all(),
        
    }
    return render(request, 'create_task.html', context)

def task_creation(request):
    if request.method == 'POST':
        task = Task.objects.create(title=request.POST['title'], description=request.POST['description'], due_date=request.POST['due_date'], creator = User.objects.get(id = request.session['user_id']))
        user = User.objects.get(id = request.POST['assigned_to'])
        task.assigned_user.add(user)
    return redirect('/all_tasks')

def delete_task(request, id):
        destroyed = Task.objects.get(id=id)
        destroyed.delete()
        return redirect('/all_tasks')



def edit(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    task = Task.objects.get(id=id)
    context = {
        'this_user':User.objects.get(id = request.session['user_id']),
        'task':task,
        'user':this_user[0],
        'users': User.objects.all(),
        'tasks':Task.objects.all()
    }
    return render(request,'edit_task.html', context)

def update_task(request, id):
    if request.method == 'POST':
        errors = Task.objects.Task_Validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/edit_task')
    edit_task = Task.objects.get(id=id)

    edit_task.due_date = request.POST['update_due_date']
    edit_task.title = request.POST['Update_Title']
    edit_task.description = request.POST['update_description']
    edit_task.save()
    return redirect('/all_tasks')

def all_tasks(request):
    context = {
        'this_user':User.objects.get(id = request.session['user_id']),
        'tasks':Task.objects.all(),
        'users': User.objects.all()
    }
    return render(request,'all_tasks.html', context)


def view_task(request, id):
    context = {
        'task':Task.objects.get(id = id),
        
}
    return render(request, 'view_task.html', context)

def complete_task(request, id):
    context = {
        'task':Task.objects.get(id = id)
    }
    return render(request,'complete_task.html', context)

def task_completion(request, id):
    if request.method == 'POST':
        complete_notes = Complete.objects.create(completion_notes = request.POST['completion_notes'], date_completed = request.POST['completion_date'], task = Task.objects.get(id = id))
    return redirect('/all_tasks')