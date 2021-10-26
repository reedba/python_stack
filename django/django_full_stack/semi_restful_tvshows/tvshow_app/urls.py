from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create_show', views.create_show),
    path('shows_list',views.shows_list),
    path('show_details/<int:show_id>',views.show_details),
    path('edit_show',views.edit_show)
]