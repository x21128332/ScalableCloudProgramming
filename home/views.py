import pyodbc
from django.shortcuts import render, redirect
from django.http import HttpResponse

def get_db_connection():
    server = 'sqlaislingsbustour.database.windows.net'
    database = 'sqlaislingsbustour'
    #using managed identity so no need fror uiser + pass
    connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlaislingsbustour.database.windows.net,1433;Database=sqlaislingsbustour;Authentication=ActiveDirectoryMsi; Encrypt=yes'
    return pyodbc.connect(connection_string)

# Create your views here.
#def index(request):
    
  #  return {"message": "Hello World"}


# Create your views here.
def index(request):
    conn = get_db_connection() 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM buses") #use parameters or apim
    rows = cursor.fetchall()
    # process rows    
    conn.close() 
   # return render(request, "home/home.html")
    context = {"rows": rows} 
    return render(request, "home/home.html", context)





