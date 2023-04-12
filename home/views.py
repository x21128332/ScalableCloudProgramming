# home views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
#def index(request):
    
  #  return {"message": "Hello World"}

def index(request):
    try:
      return render(request, "home/home.html")
    except KeyError as e:
      error_message = f"Homepage unavailable {e}"
      return render(request, "overarchingError.html", {'error_message': error_message})



