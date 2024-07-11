from django.contrib import admin
from .models import Service

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Enables viewing of services in admin section
    """
    list_display = ("service", 'price')
    search_fields = ['service']
    list_filter = ('service',)


