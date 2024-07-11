from . import views
from django.urls import path

urlpatterns = [
    path('', views.SalonIntroduction.as_view(), name='home'),
]