from django.shortcuts import render
from django.views import generic
from .models import Service

# Create your views here.

class ServiceList(generic.ListView):
    model = Service