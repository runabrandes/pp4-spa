from django.contrib import admin
from spa_home.models import Service
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Enables viewing of bookings in admin section
    """
    list_display = ('service', 'booking_date', 'booking_time', 'name', 'booking_confirmed')
    search_fields = ['booking_date', 'booking_time', 'name']
    list_filter = ('booking_date', 'booking_time', 'name',)

