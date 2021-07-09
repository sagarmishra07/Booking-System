from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showhome, name="home"),
    path('book', views.book, name="book"),
    path('menu', views.menu, name="menu"),

    
     
]