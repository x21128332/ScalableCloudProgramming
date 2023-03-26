# timetables views.py

#import pyodbc
import requests
#from prettytable import PrettyTable
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

# def get_db_connection():
#     server = 'sqlaislingsbustour.database.windows.net'
#     database = 'sqlaislingsbustour'
#     #using managed identity so no need for user + pass
#     connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlaislingsbustour.database.windows.net,1433;Database=sqlaislingsbustour;Authentication=ActiveDirectoryMsi; Encrypt=yes'
#     return pyodbc.connect(connection_string)

# # Create your views here.
# def timetables(request):
#     conn = get_db_connection() 
#     cursor = conn.cursor() 
#      #use parameters or apim 
#     cursor.execute("EXEC dbo.timetable_procedure;")
#     #cursor.execute("select [dbo].[tours].origin, [dbo].[tours].destination, [dbo].[timetables].departure_time, [dbo].[timetables].arrival_time from [dbo].[timetables] JOIN [dbo].[tours] on [dbo].[timetables].tour_id=[dbo].[tours].tour_id;")
#     rows = cursor.fetchall()
#     # Create a PrettyTable object to display the results
#     table = PrettyTable()
#     table.field_names = [desc[0] for desc in cursor.description]  # Set the column headers to the names of the columns
#     for row in rows:
#         table.add_row(row)
#     # process rows    
#     context = {"table": table} 
#     conn.close() 
#     return render(request, "timetables/timetables.html", context)

def error_view(request):
    error_code = request.GET.get('error_code')
    context = {'error_code': error_code}
    return render(request, 'error.html', context)

def timetables(request):
    try:
        # Make a GET request to a FastAPI endpoint
        response = requests.get('https://aislingsbustours-bookingapi-staging.azurewebsites.net/timetablesa')
        response.raise_for_status()
        # Get the response data as a dictionary
        data = response.json()
        # Do something with the data
        # ...
        context = {'data': data}
        return render(request, 'timetables/timetables.html', context)
    except requests.exceptions.RequestException as e:
        # handle any exceptions that occur during the request
        # return JsonResponse({'error': str(e)})
        error = error_view()
    