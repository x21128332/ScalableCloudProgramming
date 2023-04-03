# booking views.py

import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
  
def bookings(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')

        # Retrieve the booking data from the API
        response = requests.get(f'https://apimaislingsbustours.azure-api.net/bt/bookings/{booking_id}')

        if response.status_code == 200:
            mybooking = response.json()
            print(mybooking)  # print the booking data to the console

            return render(request, 'bookings/bookings.html', {'mybooking': mybooking})
        else:
            error_message = "Could not retrieve booking data"
            return render(request, 'bookings/bookings.html', {'error': error_message})
    else:
        # Retrieve the bookings data from the API
        response = requests.get('https://apimaislingsbustours.azure-api.net/bt/bookings')
    
        if response.status_code == 200:
            bookings = response.json()
            print(bookings)  # print the bookings data to the console

            return render(request, 'bookings/bookings.html', {'bookings': bookings})
        else:
            error_message = "Could not retrieve bookings data"
            return render(request, 'bookings/bookings.html', {'error': error_message})