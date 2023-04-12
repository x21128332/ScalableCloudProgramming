import requests
from django.shortcuts import render

# Create your views here.

def hotels(request):
    try:
        if request.method == "GET":
            url = f"https://apimaislingsbustours.azure-api.net/fa/accommodation?$filter=search.ismatch('Hotel','tags')"
            response = requests.get(url)

            results = response.json().get("results")
            context = {"results": results}
            return render(request, "accommodation/allhotels.html", context)
        else:
            error_message = "Could not retrieve hotel data"
            return render(request, 'accommodation/allhotels.html', {'error': error_message})
    except KeyError as e:
      error_message = f"An error occurrend {e}"
      return render(request, "overarchingError.html", {'error_message': error_message})