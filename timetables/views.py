# timetables views.py

import pyodbc
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def get_db_connection():
    server = 'sqlaislingsbustour.database.windows.net'
    database = 'sqlaislingsbustour'
    #using managed identity so no need for user + pass
    connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlaislingsbustour.database.windows.net,1433;Database=sqlaislingsbustour;Authentication=ActiveDirectoryMsi; Encrypt=yes'
    return pyodbc.connect(connection_string)

# Create your views here.
def timetables(request):
    conn = get_db_connection() 
    cursor = conn.cursor() 
     #use parameters or apim 
    cursor.execute("EXEC dbo.timetable_procedure;")
    #cursor.execute("select [dbo].[tours].origin, [dbo].[tours].destination, [dbo].[timetables].departure_time, [dbo].[timetables].arrival_time from [dbo].[timetables] JOIN [dbo].[tours] on [dbo].[timetables].tour_id=[dbo].[tours].tour_id;")
    rows = cursor.fetchall()
    # process rows    
    conn.close() 
   # return render(request, "home/home.html")
    context = {"rows": rows} 
    return render(request, "timetables/timetables.html", context)





