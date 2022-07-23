from django.http import HttpResponse
from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import booking
import customer
from customer.views import login_required_2
from venue import models as venueModel
from customer import models as customerModel
from booking import models as bookingModel
from payment import models as paymentmModel 
# Create your views here.

@login_required_2
def bookVenueForm(request, selected_venue):
    customerUsername = request.session['customerUsername']
    loggedInCustomer = customerModel.customerTable.objects.get(customerUsername=customerUsername)
    selectedVenue = venueModel.venueTable.objects.get(venueName=selected_venue)
    previousBookingsOfSelectedVenue = bookingModel.bookingTable.objects.all().filter(venueId=selectedVenue)
    bookedDateList=[]
    for booking in previousBookingsOfSelectedVenue:
        bookingDates = []
        startDate=booking.bookingStartDate
        endDate = booking.bookingEndDate
        bookingDates.append(startDate)
        bookingDates.append(endDate)
        bookedDateList.append(bookingDates)
    context = {'selected_venue': selectedVenue, 
               'loggedInCustomer':loggedInCustomer,
               'bookedDateList':bookedDateList}
    res = render(request, 'booking/bookVenueForm.html', context)
    return HttpResponse(res)


def bookVenue(request, booking_status):
    #Creating Booking Record
    newBooking = bookingModel.bookingTable()
    customer_id = request.POST['customerid']
    venue_id = request.POST['venueid'] 
    newBooking.customerId =  customerModel.customerTable.objects.get(customerId=customer_id)
    newBooking.venueId = venueModel.venueTable.objects.get(venueId=venue_id)
    newBooking.eventType = request.POST['eventtype']
    newBooking.bookingStartDate = request.POST['bookingstartdate']
    newBooking.bookingEndDate = request.POST['bookingenddate']
    newBooking.bookingDays = request.POST['totalbookingdays']
    if booking_status==1:
        newBooking.bookingStatus = "Booked"   
    newBooking.save()
    #Creating All Status Record
    allStatus = paymentmModel.allStatusTable()
    username = request.session['customerUsername']
    currentCustomer = customerModel.customerTable.objects.get(customerUsername=username)
    allStatus.customerId = currentCustomer 
    allStatus.bookingId = newBooking
    allStatus.bookingStatus = "Booked"
    allStatus.paymentStatus = "Not Paid"
    allStatus.save()
    booking_id = newBooking.bookingId
    res = "http://localhost:8000/booking/bookingdetails?bookingId={}".format(booking_id)
    return HttpResponseRedirect(res)

def showBookingDetails(request):
    currentBooking = bookingModel.bookingTable.objects.get(bookingId=request.GET['bookingId'])
    punjabiFood = bookingModel.foodTable.objects.all().filter(foodCuisine="Punjabi")
    chineseFood = bookingModel.foodTable.objects.all().filter(foodCuisine="Chinese")
    drinkFood = bookingModel.foodTable.objects.all().filter(foodCuisine="Drink")
    danceFloor = bookingModel.danceFloorTable.objects.all()  
    context = {'booking_details':currentBooking,
               'punjabi_food':punjabiFood, 
               'chinese_food':chineseFood,
               'drinks':drinkFood,
               'dance_floor':danceFloor}
    res = render(request,'booking/bookingDetailsPageWithAddOnService.html', context)
    return HttpResponse(res)

def addOnFood(request):
    D = request.session['foodid']
    food_id=request.POST['foodid']
    for foodid in D:
        if foodid==str(request.POST['foodid']):
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #To redirect to the same page
    D.append(food_id)
    request.session['foodid'] = D
    currentBooking = bookingModel.bookingTable.objects.get(bookingId=request.POST['bookingid'])
    customerFood = bookingModel.customerFoodTable()
    customerFood.bookingId = currentBooking
    customerFood.foodId = bookingModel.foodTable.objects.get(foodId=request.POST['foodid'])
    customerFood.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #To redirect to the same page

def addOnDanceFloor(request):
    D = request.session['dancefloorid']
    dancefloor_id=request.POST['dancefloorid']
    for dancefloorid in D:
        if dancefloorid==str(request.POST['dancefloorid']):
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #To redirect to the same page
    D.append(dancefloor_id)
    request.session['dancefloorid'] = D
    currentBooking = bookingModel.bookingTable.objects.get(bookingId=request.POST['bookingid'])
    customerDanceFloor = bookingModel.customerDanceFloorTable()
    customerDanceFloor.bookingId = currentBooking
    customerDanceFloor.danceFloorId = bookingModel.danceFloorTable.objects.get(danceFloorId=request.POST['dancefloorid'])
    customerDanceFloor.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #To redirect to the same page

def cancelBooking(request):
    pass

def bookVenueFormWithAddOnService(request, selected_venue, add_on):
    selectedVenue = venueModel.venueTable.objects.get(venueName=selected_venue)
    context = {'selected_venue': selectedVenue}
    res = render(request, 'booking/bookVenueFormWithAddOnService.html', context)
    return HttpResponse(res)