from django.test import TestCase
from .forms import BookingForm
from spa_home.models import Service
from .models import Booking
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta

class TestBookingForm(TestCase):

    def setUp(self):
        self.test_service = Service.objects.create(
            service="Test Service",
            description="A test service.",
            price="10.00",
        )

        #Data required for a successful booking
    
        self.required_data = {
            'service': self.test_service.id,
            'booking_date': '2024-10-28',
            'booking_time': '10:00:00',
            'booking_comments': '',
        }
        
    def create_booking(self, additional_data):
            data = self.required_data.copy()
            if additional_data:
                data.update(additional_data)
            return BookingForm(data)

    def test_booking_form_works(self):
            booking = self.create_booking(None)
            if not booking.is_valid():
                print(booking.errors)
            self.assertTrue(booking.is_valid())

