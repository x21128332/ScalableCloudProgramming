from django.shortcuts import render

# Create your views here.

def privateHire(request):
    return render(request, "privateHire/privatehire.html")