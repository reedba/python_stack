from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_game',views.create_game ),
    path('game',views.details)
]