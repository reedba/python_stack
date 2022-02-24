from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('teacher_form', views.teacher_form)
]