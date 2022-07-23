from django.urls import path
from venue import views

urlpatterns = [
    path('searchvenuebystate/', views.searchVenueByState),
    path('allvenuelist/', views.viewAllVenuesList),
    path('changevenue/<selected_venue>/', views.changeVenue),
]