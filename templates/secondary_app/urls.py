from django.urls import path
from templates.secondary_app import views

urlpatterns = [
    path('', views.index),
]