from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create_show', views.create_show),
    path('shows_list',views.shows_list),
    path('show_details/<int:show_id>',views.show_details),
    path('remove_show/<int:show_id>',views.remove_show),
    path('view_show/<int:show_id>',views.view_show ),
    path('edit_show/<int:show_id>', views.edit_show),
    path('update_show/<int:show_id>',views.update_show)
]