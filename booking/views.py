from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Booking
from spa_home.models import Service
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin

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


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    context_object_name = 'bookings'
    template_name = 'booking/booking_overview.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['bookings'] = []

        booking_upcoming = user.booking_name.all()
        for booking in booking_upcoming:
            context['bookings'].append(booking)

        return context