from django.contrib import admin
from . import models

@admin.register(models.Venue)
class VenueAdmin(admin.ModelAdmin):
    search_fields = ('name', 'address')
    ordering = ('name',) # - before attribute name to reverse ordering
    list_display = ('name', 'address', 'phone')
    fields = (('name', 'address'), 'zip_code', ('phone', 'web', 'email'))

@admin.register(models.MyUser)
class MyUserAdmin(admin.ModelAdmin):
    search_fields = ('last_name', 'first_name')
    ordering = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'email')

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('date', 'venue', 'manager')
    ordering = ('-date',)
    list_display = ('name', 'date', 'venue', 'manager')
    fields = (('name','venue'), 'date', ('manager', 'attendees'), 'description')


