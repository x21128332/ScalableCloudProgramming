# privateHire urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.privateHire, name='privateHire'),
]
