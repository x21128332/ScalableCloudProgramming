# booking views.py

import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

# def booking(request):
#     return render(request, "booking/booking.html")

# def booking(request):
#     try:
#         # Make a GET request to a FastAPI endpoint
#         response = requests.get('https://aislingsbustours-bookingapi-staging.azurewebsites.net/bookings')
#         response.raise_for_status()
#         # Get the response data as a dictionary
#         data = response.json()
#         # Do something with the data
#         # ...
#         context = {'data': data}
#         return render(request, 'booking/booking.html', context)
#     except requests.exceptions.RequestException as e:
#         # handle any exceptions that occur during the request
#         return JsonResponse({'error': str(e)})

    
# def booking(param1):
#     url = "https://aislingsbustours-bookingapi-staging.azurewebsites.net/bookings"
#     params = {"booking_id": param1}
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         result = response.json()["result"]
#         context = {"result": result}
#         return render(requests.request, "booking/booking.html", context)
#     else:
#         error_msg = f"Error: {response.status_code} {response.reason}"
#         context = {"error": error_msg}
#         return render(requests.request, "booking/booking.html", context)

def booking(request):
    try:
        if request.method == "GET":
            param1 = request.GET.get("param1")
            url = f"https://aislingsbustours-bookingapi-staging.azurewebsites.net/bookings"
            params = {"param1": param1}
            response = requests.get(url, params={'param1': param1})

            #result = response.json().get("result")
            #context = {"result": result}
            #return render(request, "booking/booking.html", context)
            return render(request, 'booking/booking.html', {'result': response.json()})
        else:
            html = "<html><body><h1>Ab errir occured!</h1></body></html>"
            return HttpResponse(html)
    except requests.exceptions.RequestException as e:
#         # handle any exceptions that occur during the request
            return JsonResponse({'error': str(e)})