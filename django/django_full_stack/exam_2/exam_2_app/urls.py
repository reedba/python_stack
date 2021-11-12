from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('wishes', views.wishes),
    path('create_wish', views.create_wish),
    path('add_wish', views.add_wish),
    path('remove_wish/<int:id>', views.remove_wish),
    path('granted/<int:id>', views.granted),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update_wish),
    path('cancel', views.cancel)
]


