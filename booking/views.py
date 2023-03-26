# booking views.py

import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

def booking(request):
    return render(request, "booking/booking.html")

def booking(request):
    try:
        # Make a GET request to a FastAPI endpoint
        response = requests.get('https://aislingsbustours-bookingapi-staging.azurewebsites.net/bookings')
        response.raise_for_status()
        # Get the response data as a dictionary
        data = response.json()
        # Do something with the data
        # ...
        context = {'data': data}
        return render(request, 'timetables/timetables.html', context)
    except requests.exceptions.RequestException as e:
        # handle any exceptions that occur during the request
        return JsonResponse({'error': str(e)})