from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('all_books', views.all_books),
    path('add_book', views.add_book),
    path('book_dets', views.book_dets),
    path('edit_book', views.edit_book)
]