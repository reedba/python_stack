from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('main_page', views.main_page),
    path('add_company', views.add_company),
    path('resume_dets/<int:id>', views.resume_dets),
]