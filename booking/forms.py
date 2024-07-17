from django import forms
from .models import Booking
from django.forms.widgets import DateInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('service', 'booking_date', 'booking_time', 'booking_comments')
        widgets = {
            'booking_date': DateInput(attrs={'type': 'date'}), 
            }
