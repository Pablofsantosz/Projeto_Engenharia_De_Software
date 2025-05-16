from django.contrib import admin
from django.urls import path
from . import views





urlpatterns = [
    path('cadastro/',views.credenciamento_cadastro,name ='cadastro'),
   
]