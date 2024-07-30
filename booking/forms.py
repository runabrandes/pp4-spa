from django import forms
from .models import Booking
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import date, datetime


class BookingForm(forms.ModelForm):
    """
    Generates the booking form for users so they can input needed information.
    """
    class Meta:
        model = Booking
        fields = (
            'service',
            'booking_date',
            'booking_time',
            'booking_comments')
        widgets = {
            'booking_date': DateInput(attrs={'type': 'date'}),
            }
        labels = {
            'service': 'Service',
            'booking_date': 'Date',
            'booking_time': 'Time',
            'booking_comments': 'Comments',
        }

# Method for validating of form fields.
    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        if booking_date < date.today():
            raise ValidationError(
                'Please select a date'
                + ' that lies ahead in the calendar.')

        if booking_date == date.today() and booking_time < datetime.now().time():
            raise ValidationError(
                'Please select'
                + ' a time that lies ahead in the calendar.')

        existing_booking = Booking.objects.filter(
            booking_date=booking_date,
            booking_time=booking_time,).exclude(id=self.instance.id)

        if existing_booking:
            raise ValidationError(
                'This appointment has already'
                + ' been booked. Please select a different timeslot.')

        return cleaned_data