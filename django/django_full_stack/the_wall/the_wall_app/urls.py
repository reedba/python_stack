from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_message', views.create_message),
    path('login_registration', views.log_reg),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout)
]