# routes views.py
import requests
from django.shortcuts import render

# Create your views here.

def routes(request):
    if request.method == 'GET':
        # Retrieve the hotels data from the API
        response = requests.get(f"https://apimaislingsbustours.azure-api.net/fa/accommodation?$filter=search.ismatch('Hotel','tags')")

        if response.status_code == 200:
            allHotels = response.json()
            print(allHotels)  # print the hotel data to the console

            return render(request, 'routes/routes.html', {'allHotels': allHotels})
        else:
            error_message = "Could not retrieve hotel data"
            return render(request, 'routes/routes.html', {'error': error_message})