
from django.shortcuts import render, redirect
from .models import Shows


def index(request):
    context = {
        'shows':Shows.objects.all()
    }
    return render(request, 'add_show.html',context)


def create_show(request):
    if request.method == 'POST':
        tv_show = Shows.objects.create(title=request.POST['title'],description=request.POST['description'],release_date=request.POST['release_date'],network=request.POST['network'])
        
    return redirect(f'/show_details/{tv_show.id}')


def shows_list(request):
    context= {
        'shows':Shows.objects.all()
    }
    return render(request,'shows_list.html',context)


def show_details(request, show_id):
    context ={
        'show':Shows.objects.get(id = show_id),
        'shows':Shows.objects.all()

    }
    return render(request,'tv_show_dets.html',context)

def view_show(request, show_id):
    show = Shows.objects.get(id = show_id)
    return redirect(f'/show_details/{show.id}')


def remove_show(request, show_id):
    show = Shows.objects.get(id = show_id)
    show.delete()
    return redirect('/shows_list')

def edit_show(request, show_id):
    context = {
        'show':Shows.objects.get(id = show_id)
    }
    return render(request,"edit_show.html", context)


def update_show(request, show_id):
    show = Shows.objects.get(id = show_id),
    show.title = request.POST['title'],
    show.description = request.POST['description'],
    show.release_date = request.POST['release_date'],
    show.network = request.POST['network'],
    show.save()
    return redirect('/shows_list')


# Create your views here.
