from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import Service


class SalonIntroduction(TemplateView, generic.ListView):
    template_name = 'spa_home/index.html'
    object_list = Service.objects.all()
