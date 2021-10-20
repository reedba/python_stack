from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('view_book/<int:book_id>',views.view_book),
    path('book_details/<int:book_id>',views.book_details),
    path('author_list',views.author_list),
    path('create_author', views.create_author),
    path('view_author/<int:author_id>',views.view_author),
    path('delete_author/<int:author_id>',views.delete_author),
    path('delete_book/<int:book_id>',views.delete_book),
    path('add_author/<int:book_id>',views.add_author),
    path('add_book/<int:author_id>',views.add_author)

    
]


