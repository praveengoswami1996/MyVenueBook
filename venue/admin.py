from django.contrib import admin
from venue.models import venueTable

# Register your models here.

class venueTableAdmin(admin.ModelAdmin):
    list_display = ['venueId','venueName','venueCity','venueState'] #We can create tuple or list

admin.site.register(venueTable, venueTableAdmin)

"""
We can also use decorator to register our model

@admin.register(venueTable)
class venueTableAdmin(admin.ModelAdmin):
    list_display = ['venueId','venueName','venueCity','venueState']
"""