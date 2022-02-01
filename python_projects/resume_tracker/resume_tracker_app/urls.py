from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('main_page', views.main_page),
    path('add_company', views.add_company),
    path("favorite/<int:company_id>", views.favorite),
    path('resume_dets/<int:id>', views.resume_dets),
    path('interview_dets/<int:id>', views.interview_dets),
    path('add_resume_dets/<int:id>', views.add_resume_dets),
    path('delete/<int:id>', views.delete_resume),
    path('edit_resume_dets/<int:id>', views.edit_resume_dets),
    path('update_resume/<int:id>', views.update_resume_dets),
    path('add_interview_dets/<int:id>', views.add_interview_dets),
    path('cancel', views.cancel),
    path('edit_interview_dets/<int:id>', views.edit_interview_dets),
    path('update_interview_dets/<int:id>', views.update_interview_dets),
    path('favorites', views.favorites)
]