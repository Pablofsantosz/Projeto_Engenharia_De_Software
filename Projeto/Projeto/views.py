from django.shortcuts import render
from django.http import HttpResponse

def projeto_login(request):
    return render (request,'login.html')