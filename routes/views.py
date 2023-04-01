# routes views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# def routes(request):
#     return render(request, "routes/routes.html")

import http.client, urllib.request, urllib.parse, urllib.error, base64

  
def routes(request):
    headers = {
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('failteireland.azure-api.net')
        conn.request("GET", "/opendata-api/v1/attractions?", headers)
        response = conn.getresponse()
        data = response.read()
        print("This is the print statement: ", data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return render(request, "routes/routes.html")