from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('view_book/<int:book_id>',views.view_book),
    path('book_details/<int:book_id>',views.book_details),
    path('author_list',views.author_list),
    path('add_author', views.add_author),
    path('view_author/<int:author_id>',views.view_author),
    
]


