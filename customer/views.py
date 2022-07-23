from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from customer import models
from booking import models as bookingModel
from payment import models as paymentModel
from venue import models as venueModel
from invoice import models as invoiceModel
import random
import datetime

# Create your views here.

def index(request):
    allVenues = venueModel.venueTable.objects.all()
    listOfRandomIndexes = random.sample(range(0, len(allVenues)), 3)
    venue1 = allVenues[listOfRandomIndexes[0]]
    venue2 = allVenues[listOfRandomIndexes[1]]
    venue3 = allVenues[listOfRandomIndexes[2]]
    context = {'venue1':venue1,'venue2':venue2, 'venue3':venue3}
    res = render(request, 'customer/index.html', context)
    return HttpResponse(res)

def customerLoginForm(request):
    allVenues = venueModel.venueTable.objects.all()
    listOfRandomIndexes = random.sample(range(0, len(allVenues)), 3)
    venue1 = allVenues[listOfRandomIndexes[0]]
    venue2 = allVenues[listOfRandomIndexes[1]]
    venue3 = allVenues[listOfRandomIndexes[2]]
    context = {'venue1':venue1,'venue2':venue2, 'venue3':venue3}
    res = render(request, 'customer/customerLoginForm.html', context)
    return HttpResponse(res)

def customerSignupForm(request):
    allVenues = venueModel.venueTable.objects.all()
    listOfRandomIndexes = random.sample(range(0, len(allVenues)), 3)
    venue1 = allVenues[listOfRandomIndexes[0]]
    venue2 = allVenues[listOfRandomIndexes[1]]
    venue3 = allVenues[listOfRandomIndexes[2]]
    context = {'venue1':venue1,'venue2':venue2, 'venue3':venue3}
    res = render(request, 'customer/customerSignupForm.html',context)
    return HttpResponse(res)

#Decorator for Login
def login_required_1(someFunction):
    def mod_someFunction(request): 
        if 'customerUsername' in request.session.keys():
            return someFunction(request)
        else:
            return HttpResponseRedirect("http://localhost:8000/customer/loginform/")
    return mod_someFunction

def login_required_2(someFunction):
    def mod_someFunction(request, selected_venue): 
        if 'customerUsername' in request.session.keys():
            return someFunction(request, selected_venue)
        else:
            return HttpResponseRedirect("http://localhost:8000/customer/loginform/")
    return mod_someFunction

#Customer Ragistration View

@login_required_1
def customerNewRegistration(request):
    customer = models.customerTable()
    alreadyCustomer = models.customerTable()
    customer.customerGender = request.POST['customergender']
    try:
        if request.FILES['customerprofileimage']:
            customer.customerImage = request.FILES['customerprofileimage']
    except:
        if customer.customerGender == "Male":
            customer.customerImage = 'media/Male-Avatar.png'
        elif customer.customerGender == "Female":
            customer.customerImage = 'media/Female-Avatar.png'
        else:
            customer.customerImage = 'media/Other-Avatar.png'
    customer.customerName = request.POST['customername']
    customer.customerDob = request.POST['customerdob']
    customer.customerEmail = request.POST['customeremail']
    customer.customerMobileCountryCode =  request.POST['customermobilecountrycode']
    customer.customerMobileNumber = request.POST['customermobilenumber']
    customer.customerAddress = request.POST['customeraddress']
    customer.customerCity = request.POST['customercity']
    customer.customerState = request.POST['customerstate']
    customer.customerPincode = request.POST['customerpincode']
    customer.customerUsername = request.POST['customerusername']
    customer.customerPassword = request.POST['customerpassword']
    context = {'customer':customer}
    flag = 0
    try:
        alreadyCustomer = models.customerTable.objects.get(customerEmail=customer.customerEmail)
        if alreadyCustomer:
            context['email_error'] = "***Email id already registered."
            flag = 1
    except alreadyCustomer.DoesNotExist:
        pass
    try:
        alreadyCustomer = models.customerTable.objects.get(customerMobileNumber=customer.customerMobileNumber)
        if alreadyCustomer:
            context['mobile_error'] = "***Mobile number already registered."
            flag = 1
    except alreadyCustomer.DoesNotExist:
        pass
    try:
        alreadyCustomer = models.customerTable.objects.get(customerUsername=customer.customerUsername)
        if alreadyCustomer:
            context['username_error'] = "***Username already taken."
            flag = 1
    except alreadyCustomer.DoesNotExist:
        pass
    if flag == 1:
        response = render(request, 'customer/customerSignupForm.html', context)
        return HttpResponse(response)            
    customer.save()
    return HttpResponseRedirect('http://localhost:8000/customer/loginform/')

@login_required_1
def customerLoginValidate(request):
    customerUsername = request.POST['customerusername']
    customerPassword = request.POST['customerpassword']
    try:
        loginUser = models.customerTable.objects.get(customerUsername=customerUsername,customerPassword=customerPassword)
        if loginUser:
            s = "http://localhost:8000/customer/dashboard/"
            request.session['customerUsername'] = customerUsername
            request.session['foodid'] = []
            request.session['dancefloorid'] = []
    except:
         s = "http://localhost:8000/customer/loginform/"
    return HttpResponseRedirect(s)  

@login_required_1
def customerDashboard(request):
    allVenues = venueModel.venueTable.objects.all()
    listOfRandomIndexes = random.sample(range(0, len(allVenues)), 3)
    venue1 = allVenues[listOfRandomIndexes[0]]
    venue2 = allVenues[listOfRandomIndexes[1]]
    venue3 = allVenues[listOfRandomIndexes[2]]
    username = request.session['customerUsername']
    currentCustomer = models.customerTable.objects.get(customerUsername=username)
    try:
        bookingRecords = paymentModel.allStatusTable.objects.all().filter(customerId=currentCustomer)
        numberOfRecords = len(bookingRecords)
        customerRecentBooking = bookingRecords[numberOfRecords-1]
        context = {'venue1':venue1, 'venue2':venue2, 'venue3':venue3,
                    'recentBooking':customerRecentBooking}
    except:
        context = {'venue1':venue1, 'venue2':venue2, 'venue3':venue3,}
    res = render(request,'customer/customerDashboardAfterLogin.html', context)
    return HttpResponse(res)

@login_required_1
def customerBookingRecords(request):
    username = request.session['customerUsername']
    currentCustomer = models.customerTable.objects.get(customerUsername=username)
    bookingRecords = paymentModel.allStatusTable.objects.all().filter(customerId=currentCustomer)
    context = {'bookingRecords':bookingRecords}
    res = render(request,'customer/customerBookingRecords.html',context)
    return HttpResponse(res)

@login_required_1
def searchVenueByState(request):
    venueState = request.POST['venuestate']
    venueCity = request.POST['venuecity']
    allVenues = venueModel.venueTable.objects.filter(venueState = venueState, venueCity = venueCity)
    context = {'venues':allVenues,
              'listbyState':True}
    res = render(request,'customer/customerSearchVenueByState.html',context)
    return HttpResponse(res)

@login_required_1
def showAllVenueList(request):
    venues = venueModel.venueTable.objects.all()
    context = {'venues':venues}
    res = render(request, 'customer/showAllVenuesList.html', context)
    return HttpResponse(res)

@login_required_1
def myProfile(request):
    username = request.session['customerUsername']
    currentCustomer = models.customerTable.objects.get(customerUsername = username)
    context = {'customer':currentCustomer}
    response = render(request, 'customer/myProfilePage.html', context)
    return HttpResponse(response)

@login_required_1
def saveCustomerProfile(request):
    customer = models.customerTable()
    customerList = models.customerTable()
    customer.customerId = request.POST['customerid']
    customer.customerName = request.POST['customername']
    try:
        if request.FILES['customerprofileimage']:
            customer.customerImage = request.FILES['customerprofileimage']
    except:
        customer.customerImage = request.POST['previousprofileimage']
    try:
        if request.POST['customergender']:
            customer.customerGender = request.POST['customergender']
    except:
        customer.customerGender = request.POST['previousgendervalue']
    
    newDateOfBirth = request.POST['customerdob']
    if newDateOfBirth:
        customer.customerDob = request.POST['customerdob']
    else:
        customer.customerDob = request.POST['previousdobdate']
        
    customer.customerEmail = request.POST['customeremail']
    customer.customerMobileCountryCode =  request.POST['customermobilecountrycode']
    customer.customerMobileNumber = request.POST['customermobilenumber']
    customer.customerAddress = request.POST['customeraddress']
    customer.customerCity = request.POST['customercity']
    customer.customerState = request.POST['customerstate']
    customer.customerPincode = request.POST['customerpincode']
    customer.customerUsername = request.POST['customerusername']
    customer.customerPassword = request.POST['customerpassword']
    context = {'customer':customer}
    flag = 0
    try:
        customerList = models.customerTable.objects.exclude(customerId = customer.customerId)
        for customerX in customerList:
            if customerX.customerEmail == customer.customerEmail:
                context['email_error'] = "***Email id already registered."
                flag = 1
                break
    except:
        pass
    try:
        customerList = models.customerTable.objects.exclude(customerId = customer.customerId)
        for customerY in customerList:
            if customerY.customerMobileNumber == customer.customerMobileNumber:
                context['mobile_error'] = "***Mobile number already registered."
                flag = 1
                break
    except:
        pass
    try:
        customerList = models.customerTable.objects.exclude(customerId = customer.customerId)
        for customerZ in customerList:
            if customerZ.customerUsername == customer.customerUsername:
                context['username_error'] = "***Username already taken."
                flag = 1
                break
    except:
        pass
    if flag == 1:
        response = render(request, 'customer/myProfilePage.html', context)
        return HttpResponse(response)            
    customer.save()
    return HttpResponseRedirect('http://localhost:8000/customer/myprofile/')

@login_required_1
def myInvoices(request):
    username = request.session['customerUsername']
    currentCustomer = models.customerTable.objects.get(customerUsername = username)
    try:
        invoiceRecord = invoiceModel.invoiceTable.objects.filter(customerId = currentCustomer)
        context = {'invoices':invoiceRecord}
    except:
        context = {}
    response = render(request, 'customer/customerInvoiceRecord.html', context)
    return HttpResponse(response)

@login_required_1
def customerFeedbackForm(request):
    username = request.session['customerUsername']
    currentCustomer = models.customerTable.objects.get(customerUsername = username)
    context = {'customerId':currentCustomer.customerId}
    response = render(request, 'customer/customerFeedbackForm.html', context)
    return HttpResponse(response)

@login_required_1
def submitFeedback(request):
    newFeedback = models.feedbackTable()
    currentCustomer = models.customerTable.objects.get(customerId = int(request.POST['customerid'])) 
    newFeedback.customerId = currentCustomer
    newFeedback.feedbackType = request.POST['feedbacktype']
    newFeedback.feedbackDescription = request.POST['feedbackdescription']
    newFeedback.feedbackStatus = "Not Replied"
    newFeedback.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def myFeedbacks(request):
    username = request.session['customerUsername']
    currentCustomer = models.customerTable.objects.get(customerUsername = username)
    try:
        feedbackRecord = models.feedbackTable.objects.filter(customerId = currentCustomer) 
        context = {'feedbacks': feedbackRecord}
    except:
        pass
    response = render(request, 'customer/customerFeedbackRecord.html', context)
    return HttpResponse(response)

@login_required_1
def deleteMyAccount(request):
    username = request.session['customerUsername']
    receivedPassword = request.POST['customerpassword']
    currentCustomer = models.customerTable.objects.get(customerUsername = username)
    if currentCustomer.customerPassword == receivedPassword:
        currentCustomer.delete()
        del request.session['customerUsername']
        return HttpResponseRedirect("http://localhost:8000/customer/loginform/")
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required_1
def customerLogout(request):
    del request.session['customerUsername']
    return HttpResponseRedirect("http://localhost:8000/")