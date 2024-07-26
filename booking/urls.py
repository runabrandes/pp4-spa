from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.booking_request, name='booking'),
    path('booking_overview', views.BookingListView.as_view(), name='booking_overview'),
]