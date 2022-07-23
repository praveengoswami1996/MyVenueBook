from django.urls import path
from booking import views

urlpatterns = [
    path('bookvenueform/<selected_venue>/',views.bookVenueForm),
    path('bookingdetails/',views.showBookingDetails),
    path('addonfood/',views.addOnFood),
    path('addondancefloor/',views.addOnDanceFloor),
    path('cancelbooking/', views.cancelBooking),
    path('bookvenue/<int:booking_status>/',views.bookVenue),
    path('bookvenueform/<selected_venue>/<add_on>/',views.bookVenueFormWithAddOnService),
]