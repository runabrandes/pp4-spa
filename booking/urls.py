from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.booking_request, name='booking'),
    path('booking_overview', views.BookingListView.as_view(), name='booking_overview'),
    path('cancel/<int:booking_id>', views.cancel_booking, name='cancel_booking'),
    path('past_bookings', views.PastBookingListView.as_view(), name='past_bookings'),
    path('edit/<int:booking_id>', views.edit_booking, name='edit_booking'),
]