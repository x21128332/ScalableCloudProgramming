# privateHire views.py

from django.shortcuts import render

# Create your views here.

def privatehire(request):
    return render(request, "privateHire/privatehire.html")