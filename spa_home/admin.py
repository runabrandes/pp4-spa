from django.contrib import admin
from .models import Service, Booking

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Enables viewing of services in admin section
    """
    list_display = ("service", 'price')
    search_fields = ['service']
    list_filter = ('service',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Enables viewing of bookings in admin section
    """
    list_display = ('service', 'booking_date', 'booking_time', 'name', 'booking_confirmed')
    search_fields = ['booking_date', 'booking_time', 'name']
    list_filter = ('booking_date', 'booking_time', 'name',)