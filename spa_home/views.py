from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Service

# Create your views here.
class SalonIntroduction(TemplateView, generic.ListView):
     template_name = 'spa_home/index.html'
     object_list = Service.objects.all()
