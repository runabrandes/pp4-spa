from django.shortcuts import render
from django.contrib import messages
from .models import Booking
from spa_home.models import Service
from .forms import BookingForm

# Create your views here.

def booking_request(request):
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.name = request.user
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, "Many thanks for booking an appointment. We look forward to seeing you at Mountain Mist Spa!")

    booking_form = BookingForm()

    return render(
        request,
        'booking/booking.html',
        {'booking_form': booking_form},
    )