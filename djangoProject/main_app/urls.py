from django.urls import path
from djangoProject.main_app import views

urlpatterns = [
    path('', views.index),
]