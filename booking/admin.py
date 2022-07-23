from django.contrib import admin
from booking.models import bookingTable, foodTable, danceFloorTable, customerFoodTable, customerDanceFloorTable

# Register your models here.
class bookingTableAdmin(admin.ModelAdmin):
    list_display = ['bookingId','customerId', 'venueId','bookingStatus']

class foodTableAdmin(admin.ModelAdmin):
    list_display = ['foodId','foodName','foodCuisine','foodPricePerServing','foodCode']

class danceFloorTableAdmin(admin.ModelAdmin):
    list_display = ['danceFloorId','danceFloorType', 'danceFloorPricePerBooking', 'danceFloorCode']

class customerFoodTableAdmin(admin.ModelAdmin):
    list_display = ['bookingId','foodId']

class customerDanceFloorTableAdmin(admin.ModelAdmin):
    list_display = ['bookingId','danceFloorId']

admin.site.register(bookingTable, bookingTableAdmin)
admin.site.register(foodTable, foodTableAdmin)
admin.site.register(danceFloorTable, danceFloorTableAdmin)
admin.site.register(customerFoodTable, customerFoodTableAdmin)
admin.site.register(customerDanceFloorTable, customerDanceFloorTableAdmin)