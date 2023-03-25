# routes views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def routes(request):
    return render(request, "routes/routes.html")


