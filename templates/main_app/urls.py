from django.urls import path
from templates.main_app import views

urlspatterns = [
    path('', views.index),
]