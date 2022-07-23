from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from venue import models
import random

# Create your views here.
def searchVenueByState(request):
    allVenues = models.venueTable.objects.all()
    listOfRandomIndexes = random.sample(range(0, len(allVenues)), 3)
    venue1 = allVenues[listOfRandomIndexes[0]]
    venue2 = allVenues[listOfRandomIndexes[1]]
    venue3 = allVenues[listOfRandomIndexes[2]]
    venueState = request.POST['venuestate']
    venueCity = request.POST['venuecity']
    allVenues = models.venueTable.objects.filter(venueState = venueState, venueCity = venueCity)
    context = {'venue1':venue1,'venue2':venue2, 'venue3':venue3, 'venues':allVenues,
              'listbyState':True}
    res = render(request,'venue/searchVenueByState.html',context)
    return HttpResponse(res)

def changeVenue(request, selected_venue):
    allVenues = models.venueTable.objects.all()
    listOfRandomIndexes = random.sample(range(0, len(allVenues)), 3)
    venue1 = allVenues[listOfRandomIndexes[0]]
    venue2 = allVenues[listOfRandomIndexes[1]]
    venue3 = allVenues[listOfRandomIndexes[2]]
    selectedVenue = models.venueTable.objects.get(venueName=selected_venue)
    venueCity = selectedVenue.venueCity
    allVenues = models.venueTable.objects.filter(venueCity = venueCity)
    context = {'venue1':venue1,'venue2':venue2, 'venue3':venue3,'venues':allVenues,
              'allvenuelist':True}
    res = render(request, 'venue/searchVenueByState.html',context)
    return HttpResponse(res)

def viewAllVenuesList(request):
    allVenues = models.venueTable.objects.all()
    listOfRandomIndexes = random.sample(range(0, len(allVenues)), 3)
    venue1 = allVenues[listOfRandomIndexes[0]]
    venue2 = allVenues[listOfRandomIndexes[1]]
    venue3 = allVenues[listOfRandomIndexes[2]]
    venues = models.venueTable.objects.all()
    context = {'venue1':venue1,'venue2':venue2, 'venue3':venue3,'venues':venues}
    res = render(request, 'venue/viewAllVenuesList.html', context)
    return res

 