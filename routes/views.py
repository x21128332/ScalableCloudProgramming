# routes views.py
# from django.shortcuts import render, redirect
# from django.http import HttpResponse

# Create your views here.
# def routes(request):
#     return render(request, "routes/routes.html")

# import http.client, urllib.request, urllib.parse, urllib.error, json
  
# def routes(request):
#     params = urllib.parse.urlencode({
#     })

#     try:
#         conn = http.client.HTTPSConnection('failteireland.azure-api.net')
#         conn.request("GET", "/opendata-api/v1/attractions")
#         response = conn.getresponse()
#         data = response.read()
#         data_dict = json.loads(data)
#         print("This is the print statement: ", data_dict)
#         conn.close()
#     except Exception as e:
#         print("[Errno {0}] {1}".format(e.errno, e.strerror))
#     return render(request, "routes/routes.html", data_dict)

import requests
from django.shortcuts import render

def routes(request):
    try:
        # Make a request to the API to get hotels
        url = "https://apimaislingsbustours.azure-api.net/fa/accommodation?$filter=search.ismatch('Hotel','tags')"
        #add headers to the request
        #headers = {'Ocp-Apim-Subscription-Key': '5b76885a3e814b2c9982549f3d9f0559'}
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code != 200:
           return render(request, 'routes/routes.html')
        # Parse the response JSON
        hotels = response.json()['hotels'][:5]
        # Render the template with the hotels
        return render(request, 'routes/routes.html', {'hotels': hotels})
    
    except KeyError as e:
        error_message = f"Routes page is unavailable {e}"
        return render(request, "overarchingError.html", {'error_message': error_message})