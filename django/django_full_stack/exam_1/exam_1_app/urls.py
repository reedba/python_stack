from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('create_quote', views.create_quote),
    path('like/<int:id>', views.add_like),
    path('poster_list/<int:id>', views.poster_list),
    path('delete/<int:id>', views.delete_quote),
    path('edit_account/<int:id>', views.edit_account),
    path('update', views.update)
]