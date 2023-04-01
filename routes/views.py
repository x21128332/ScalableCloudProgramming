# routes views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# def routes(request):
#     return render(request, "routes/routes.html")

import http.client, urllib.request, urllib.parse, urllib.error, json
  
def routes(request):
    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('failteireland.azure-api.net')
        conn.request("GET", "/opendata-api/v1/attractions")
        response = conn.getresponse()
        data = response.read()
        data_dict = json.loads(data)
        print("This is the print statement: ", data_dict)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return render(request, "routes/routes.html", data_dict)