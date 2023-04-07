# booking urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('', views.booking, name='create_passenger'),
]
