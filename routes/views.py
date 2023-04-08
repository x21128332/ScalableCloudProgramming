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
        # Make a request to the API to get attractions
        url = 'https://failteireland.azure-api.net/opendata-api/v1/attractions'
        response = requests.get(url)
        # Check if the response was successful
        if response.status_code != 200:
            error_message = f"Request failed with status code {response.status_code}: {response.text}"
            return render(request, 'attractions/error.html', {'error_message': error_message})
        # Parse the response JSON
        try:
            attractions = response.json()['attractions'][:5]
        except KeyError as e:
            error_message = f"Response missing required key: {e}"
            return render(request, 'routes/error.html', {'error_message': error_message})

        # Render the template with the attractions
        return render(request, 'routes/routes.html', {'attractions': attractions})
    
    except KeyError as e:
        error_message = f"Routes page is unavailable {e}"
        return render(request, "overarchingError.html", {'error_message': error_message})



