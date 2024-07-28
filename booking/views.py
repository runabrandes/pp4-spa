from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Booking
from spa_home.models import Service
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, time, datetime

# Create your views here.

def booking_request(request):
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.name = request.user
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, "Many thanks for booking an appointment. We look forward to seeing you at Mountain Mist Spa!")
        else:
            for field, errors in booking_form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")


    booking_form = BookingForm()

    return render(
        request,
        'booking/booking.html',
        {'booking_form': booking_form},
    )


class BookingListView(LoginRequiredMixin, ListView):
    """
    View to output and filter bookings.
    Only shows bookings in the future.
    """
    model = Booking
    context_object_name = 'bookings'
    template_name = 'booking/booking_overview.html'

    #Show bookings in bookings_overview and filter only upcoming bookings
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        today = datetime.now()
        context['bookings'] = []

        booking_upcoming = user.booking_name.all()
        context['bookings'] = booking_upcoming.filter(booking_date__gte=today.date())

        return context



def cancel_booking(request, booking_id):
        """
        Function to cancel bookings made.
        """
        queryset = Booking.objects.filter(name=request.user)
        booking_to_cancel = get_object_or_404(queryset, id=booking_id)

        if booking_to_cancel.name == request.user:
            booking_to_cancel.delete()
            messages.add_message(request, messages.SUCCESS, 'Booking cancelled!')
        else:
            messages.add_message(request, messages.ERROR, 'Cancellation unsuccessful. Please call Mountain Mist Spa for assistance.')

        return HttpResponseRedirect(reverse('booking_overview'))


def edit_booking(request, booking_id):
    """
    Function to edit existing bookings 
    """
    queryset = Booking.objects.filter(name=request.user)
    booking_to_edit = get_object_or_404(queryset, id=booking_id)

    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking_to_edit)
        if booking_form.is_valid():
            booking_to_edit.booking_confirmed = False
            booking_form.save()
            messages.success(request, 'Appointment updated successfully.')
            return HttpResponseRedirect(reverse('booking_overview'))
        else:
            messages.error(request, 'Update unsuccessful. Please call Mountain Mist Spa for assistance.')

    booking_form = BookingForm(instance=booking_to_edit)

    return render(request, 'booking/booking_update.html', {'booking_form': booking_form})


    
class PastBookingListView(LoginRequiredMixin, ListView):
    """
    View to output and filter bookings.
    Only shows bookings in the future.
    """
    model = Booking
    context_object_name = 'bookings'
    template_name = 'booking/past_bookings.html'

    #Show bookings in bookings_overview and filter only upcoming bookings
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        today = datetime.now()
        context['bookings'] = []

        booking_upcoming = user.booking_name.all()
        context['bookings'] = booking_upcoming.filter(booking_date__lte=today.date())

        return context