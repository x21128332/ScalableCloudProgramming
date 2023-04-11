import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def hotels(request):
    try:
        if request.method == "GET":
            url = f"https://apimaislingsbustours.azure-api.net/fa/accommodation?$filter=search.ismatch('Hotel','tags')"
            response = requests.get(url)

            results = response.json().get("results")
            context = {"results": results}
            return render(request, "accommodation/allhotels", context)
        else:
            html = "<html><body><h1>An error occured!</h1></body></html>"
            return HttpResponse(html)
    except requests.exceptions.RequestException as e:
          # handle any exceptions that occur during the request
            return JsonResponse({'error': str(e)})
