from turtle import home
from django.urls import path

from . import views

urlpatterns = [
    path("index", views.home),
    path("random_info_page", views.random_method),
    path("<str:name>", views.index)
]