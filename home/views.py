from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Hello World")


#def index(request):
#    return HttpResponse("Hello, world. You're at the Cats index.")
# Create your views here.
def index(request):
    return render(request, "home/home.html")