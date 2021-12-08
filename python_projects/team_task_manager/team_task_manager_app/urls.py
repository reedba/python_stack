from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('create_task',views.create_task),
    path('task_creation', views.task_creation),
    path('cat_creation', views.cat_creation),
    path('edit_task', views.edit_task),
    path('all_tasks', views.all_tasks),
    path('complete_task', views.complete_task),
    path('view_task', views.view_task),
    
]