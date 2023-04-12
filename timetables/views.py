# timetables views.py

import requests
from django.shortcuts import render

def timetables(request):
    try:
        # Retrieve the timetable data from the API
        response = requests.get('https://apimaislingsbustours.azure-api.net/bt/timetables')
        
        if response.status_code == 200:
            timetables = response.json()
            print(timetables)  # print the timetable data to the console

            return render(request, 'timetables/timetables.html', {'timetables': timetables})
        else:
            error_message = "Could not retrieve timetables data"
            return render(request, 'timetables/timetables.html', {'error': error_message})
    except KeyError as e:
      error_message = f"Timetables unavailable {e}"
      return render(request, "overarchingError.html", {'error_message': error_message})


