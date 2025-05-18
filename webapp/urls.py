from django.contrib import admin
from django.urls import path
from . import views





urlpatterns = [
    path('homepage/',views.webapp_homepage,name ='homepage'),
    path('perfil/',views.webapp_perfil,name ='perfil'),
    path('excluir/',views.web_delete, name ='excluir')
   
]