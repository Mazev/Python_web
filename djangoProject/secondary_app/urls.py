from django.urls import path
from djangoProject.secondary_app import views

urlpatterns = [
    path('', views.index),
]