from django.db import models
from django.contrib.auth.models import User
from spa_home.models import Service
from cloudinary.models import CloudinaryField
import datetime

# Create your models here.

BOOKING_TIMESLOTS = (
    (datetime.time(10, 0, 0), "10:00"),
    (datetime.time(11, 0, 0), "11:00"),
    (datetime.time(12, 0, 0), "12:00"),
    (datetime.time(13, 0, 0), "13:00"),
    (datetime.time(14, 0, 0), "14:00"),
    (datetime.time(15, 0, 0), "15:00"),
    (datetime.time(16, 0, 0), "16:00"),
    (datetime.time(17, 0, 0), "17:00"),
    (datetime.time(18, 0, 0), "18:00"),
)


class Booking(models.Model):
    """
    Model for making bookings.
    """

    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booking_name")
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="booking_service")
    date_booking_made = models.DateField(auto_now_add=True)
    booking_date = models.DateField()
    booking_time = models.TimeField(choices=BOOKING_TIMESLOTS)
    booking_confirmed = models.BooleanField(default=False)
    booking_comments = models.TextField(blank=True)

    class Meta:
        ordering = ['booking_date', 'booking_time']

    def __str__(self):
        return (f"{self.name} booked {self.service} on"
                + "{self.booking_date} at {self.booking_time}")
