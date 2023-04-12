# routes views.py
from django.shortcuts import render

# Create your views here.

def routes(request):
        return render(request, 'routes/routes.html')