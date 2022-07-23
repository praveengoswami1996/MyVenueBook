from ast import Pass
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import administrator
from customer import models as customerModel
from administrator import models as adminModel
from venue import models as venueModel
from payment import models as paymentModel
from invoice import models as invoiceModel
from booking import models as bookingModel

# Create your views here.

#Decorator for Login
def login_required_1(someFunction):
    def mod_someFunction(request): 
        if 'adminUsername' in request.session.keys():
            return someFunction(request)
        else:
            return HttpResponseRedirect("http://localhost:8000/administrator/")
    return mod_someFunction

def adminLoginForm(request):
    res = render(request,'administrator/adminLoginForm.html')
    return HttpResponse(res)

def adminLoginValidate(request):
    adminUsername = request.POST['adminusername']
    adminPassword = request.POST['adminpassword']
    try:
        loginAdmin = adminModel.administratorTable.objects.get(adminUsername=adminUsername, adminPassword=adminPassword) 
        if loginAdmin:
            s="http://localhost:8000/administrator/dashboard/"
            request.session['adminUsername'] = adminUsername 
    except:
        s="http://localhost:8000/administrator/"
    return HttpResponseRedirect(s)

@login_required_1
def adminLogout(request):
    del request.session['adminUsername']
    return HttpResponseRedirect("http://localhost:8000/administrator/")

def adminSignupForm(request):
    res = render(request, 'administrator/adminSignupForm.html')
    return HttpResponse(res)

@login_required_1
def addMessage(request):
    newMessage = adminModel.messageTable()
    newMessage.senderName = request.POST['sendername']
    newMessage.senderEmail = request.POST['senderemail']
    newMessage.senderMessage = request.POST['sendermessage']
    newMessage.messageStatus = request.POST['messagestatus']
    newMessage.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def showAllMessages(request):
    allMessages = adminModel.messageTable.objects.all()
    context = {'messages':allMessages}
    response = render(request, 'administrator/allMessageRecord.html', context)
    return HttpResponse(response)

@login_required_1
def changeMessageStatus(request):
    messageToBeUpdated = adminModel.messageTable.objects.get(messageId = int(request.POST['messageid']))
    messageToBeUpdated.messageStatus = request.POST['messagestatus']
    messageToBeUpdated.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def adminDashboard(request):
    res = render(request, 'administrator/adminDashboard.html')
    return HttpResponse(res)

@login_required_1
def viewAllCustomer(request):
    allCustomers = customerModel.customerTable.objects.all()
    context = {'allCustomers':allCustomers}
    res = render(request,'administrator/viewAllCustomer.html',context)
    return HttpResponse(res) 

@login_required_1
def showAddCustomerForm(request):
    response = render(request, 'administrator/addCustomerForm.html')
    return HttpResponse(response)

@login_required_1
def addCustomer(request):
    customer = customerModel.customerTable()
    alreadyCustomer = customerModel.customerTable()
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
        alreadyCustomer = customerModel.customerTable.objects.get(customerEmail=customer.customerEmail)
        if alreadyCustomer:
            context['email_error'] = "***Email id already registered."
            flag = 1
    except alreadyCustomer.DoesNotExist:
        pass
    try:
        alreadyCustomer = customerModel.customerTable.objects.get(customerMobileNumber=customer.customerMobileNumber)
        if alreadyCustomer:
            context['mobile_error'] = "***Mobile number already registered."
            flag = 1
    except alreadyCustomer.DoesNotExist:
        pass
    try:
        alreadyCustomer = customerModel.customerTable.objects.get(customerUsername=customer.customerUsername)
        if alreadyCustomer:
            context['username_error'] = "***Username already taken."
            flag = 1
    except alreadyCustomer.DoesNotExist:
        pass
    if flag == 1:
        response = render(request, 'administrator/addCustomerForm.html', context)
        return HttpResponse(response)            
    customer.save()
    return HttpResponseRedirect('http://localhost:8000/administrator/viewallcustomer/')

def showEditCustomerPage(request, customer_id):
    customerToBeEdited = customerModel.customerTable.objects.get(customerId=customer_id)
    context = {'customer':customerToBeEdited}
    res = render(request, 'administrator/editCustomerPage.html',context)
    return HttpResponse(res)

@login_required_1
def updateCustomer(request):
    updatedCustomer = customerModel.customerTable()
    customerList = customerModel.customerTable()
    updatedCustomer.customerId = request.POST['customerid']
    updatedCustomer.customerName = request.POST['customername']
    try:
        if request.FILES['customerprofileimage']:
            updatedCustomer.customerImage = request.FILES['customerprofileimage']
    except:
        updatedCustomer.customerImage = request.POST['previousprofileimage']
    try:
        if request.POST['customergender']:
            updatedCustomer.customerGender = request.POST['customergender']
    except:
        updatedCustomer.customerGender = request.POST['previousgendervalue']
    
    newDateOfBirth = request.POST['customerdob']
    if newDateOfBirth:
        updatedCustomer.customerDob = request.POST['customerdob']
    else:
        updatedCustomer.customerDob = request.POST['previousdobdate']
        
    updatedCustomer.customerEmail = request.POST['customeremail']
    updatedCustomer.customerMobileCountryCode =  request.POST['customermobilecountrycode']
    updatedCustomer.customerMobileNumber = request.POST['customermobilenumber']
    updatedCustomer.customerAddress = request.POST['customeraddress']
    updatedCustomer.customerCity = request.POST['customercity']
    updatedCustomer.customerState = request.POST['customerstate']
    updatedCustomer.customerPincode = request.POST['customerpincode']
    updatedCustomer.customerUsername = request.POST['customerusername']
    updatedCustomer.customerPassword = request.POST['customerpassword']
    context = {'customer':updatedCustomer}
    flag = 0
    try:
        customerList = customerModel.customerTable.objects.exclude(customerId = updatedCustomer.customerId)
        for customerX in customerList:
            if customerX.customerEmail == updatedCustomer.customerEmail:
                context['email_error'] = "***Email id already registered."
                flag = 1
                break
    except:
        pass
    try:
        customerList = customerModel.customerTable.objects.exclude(customerId = updatedCustomer.customerId)
        for customerY in customerList:
            if customerY.customerMobileNumber == updatedCustomer.customerMobileNumber:
                context['mobile_error'] = "***Mobile number already registered."
                flag = 1
                break
    except:
        pass
    try:
        customerList = customerModel.customerTable.objects.exclude(customerId = updatedCustomer.customerId)
        for customerZ in customerList:
            if customerZ.customerUsername == updatedCustomer.customerUsername:
                context['username_error'] = "***Username already taken."
                flag = 1
                break
    except:
        pass
    if flag == 1:
        response = render(request, 'administrator/editCustomerPage.html', context)
        return HttpResponse(response)            
    updatedCustomer.save()
    return HttpResponseRedirect('http://localhost:8000/administrator/viewallcustomer/')

def deleteCustomer(request, customer_id):
    customerToBeDeleted = customerModel.customerTable.objects.get(customerId=customer_id)
    customerToBeDeleted.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def showAddAdministratorForm(request):
    res = render(request,'administrator/addAdministratorForm.html')
    return HttpResponse(res)

@login_required_1
def addAdministrator(request):
    admin = adminModel.administratorTable()
    alreadyAdmin = adminModel.administratorTable()
    admin.adminGender = request.POST['admingender']
    try:
        if request.FILES['adminprofileimage']:
            admin.adminImage = request.FILES['adminprofileimage']
    except:
        if admin.adminGender == "Male":
            admin.adminImage = 'media/Male-Avatar.png'
        elif admin.adminGender == "Female":
            admin.adminImage = 'media/Female-Avatar.png'
        else:
            admin.adminImage = 'media/Other-Avatar.png'
    admin.adminName = request.POST['adminname']
    admin.adminDob = request.POST['admindob']
    admin.adminDesignation = request.POST['admindesignation']
    admin.adminEmail = request.POST['adminemail']
    admin.adminMobileCountryCode =  request.POST['adminmobilecountrycode']
    admin.adminMobileNumber = request.POST['adminmobilenumber']
    admin.adminAddress = request.POST['adminaddress']
    admin.adminUsername = request.POST['adminusername']
    admin.adminPassword = request.POST['adminpassword']
    context = {'admin':admin}
    flag = 0
    try:
        alreadyAdmin = adminModel.administratorTable.objects.get(adminEmail=admin.adminEmail)
        if alreadyAdmin:
            context['email_error'] = "***Email id already registered."
            flag = 1
    except alreadyAdmin.DoesNotExist:
        pass
    try:
        alreadyAdmin = adminModel.administratorTable.objects.get(adminMobileNumber=admin.adminMobileNumber)
        if alreadyAdmin:
            context['mobile_error'] = "***Mobile number already registered."
            flag = 1
    except alreadyAdmin.DoesNotExist:
        pass
    try:
        alreadyAdmin = adminModel.administratorTable.objects.get(adminUsername=admin.adminUsername)
        if alreadyAdmin:
            context['username_error'] = "***Username already taken."
            flag = 1
    except alreadyAdmin.DoesNotExist:
        pass
    if flag == 1:
        response = render(request, 'administrator/addAdministratorForm.html', context)
        return HttpResponse(response)            
    admin.save()
    return HttpResponseRedirect('http://localhost:8000/administrator/viewalladministrator/')


def showEditAdministratorPage(request, admin_id):
    adminTobeEdited = adminModel.administratorTable.objects.get(adminId=admin_id)
    context = {'admin':adminTobeEdited}
    res = render(request, 'administrator/editAdministratorPage.html',context)
    return HttpResponse(res)

@login_required_1
def updateAdministrator(request):
    updatedAdmin = adminModel.administratorTable()
    adminList = adminModel.administratorTable()
    updatedAdmin.adminId = request.POST['adminid']
    updatedAdmin.adminName = request.POST['adminname']
    try:
        if request.FILES['adminprofileimage']:
            updatedAdmin.adminImage = request.FILES['adminprofileimage']
    except:
        updatedAdmin.adminImage = request.POST['previousprofileimage']
    try:
        if request.POST['admingender']:
            updatedAdmin.adminGender = request.POST['admingender']
    except:
        updatedAdmin.adminGender = request.POST['previousgendervalue']
    
    newDateOfBirth = request.POST['admindob']
    if newDateOfBirth:
        updatedAdmin.adminDob = request.POST['admindob']
    else:
        updatedAdmin.adminDob = request.POST['previousdobdate']

    updatedAdmin.adminDesignation = request.POST['admindesignation']    
    updatedAdmin.adminEmail = request.POST['adminemail']
    updatedAdmin.adminMobileCountryCode =  request.POST['adminmobilecountrycode']
    updatedAdmin.adminMobileNumber = request.POST['adminmobilenumber']
    updatedAdmin.adminAddress = request.POST['adminaddress']
    updatedAdmin.adminUsername = request.POST['adminusername']
    updatedAdmin.adminPassword = request.POST['adminpassword']
    context = {'admin':updatedAdmin}
    flag = 0
    try:
        adminList = adminModel.administratorTable.objects.exclude(adminId = updatedAdmin.adminId)
        for adminX in adminList:
            if adminX.adminEmail == updatedAdmin.adminEmail:
                context['email_error'] = "***Email id already registered."
                flag = 1
                break
    except:
        pass
    try:
        adminList = adminModel.administratorTable.objects.exclude(adminId = updatedAdmin.adminId)
        for adminY in adminList:
            if adminY.adminMobileNumber == updatedAdmin.adminMobileNumber:
                context['mobile_error'] = "***Mobile number already registered."
                flag = 1
                break
    except:
        pass
    try:
        adminList = adminModel.administratorTable.objects.exclude(adminId = updatedAdmin.adminId)
        for adminZ in adminList:
            if adminZ.adminUsername == updatedAdmin.adminUsername:
                context['username_error'] = "***Username already taken."
                flag = 1
                break
    except:
        pass
    if flag == 1:
        response = render(request, 'administrator/editAdministratorPage.html', context)
        return HttpResponse(response)            
    updatedAdmin.save()
    return HttpResponseRedirect('http://localhost:8000/administrator/viewalladministrator/')


def deleteAdministrator(request, admin_id):
    adminToBeDeleted = adminModel.administratorTable.objects.get(adminId=admin_id)
    adminToBeDeleted.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def viewAllAdmin(request):
    alladmins = adminModel.administratorTable.objects.all()
    context = {'alladmins':alladmins}
    res = render(request,'administrator/viewAllAdmin.html',context)
    return HttpResponse(res)

@login_required_1
def showAddVenueForm(request):
    res = render(request, "administrator/addVenueForm.html")
    return HttpResponse(res)

@login_required_1
def addVenue(request):
    newVenue = venueModel.venueTable()
    newVenue.venueName = request.POST['venuename']
    newVenue.venueDescription = request.POST['venuedescription']
    newVenue.venueCity = request.POST['city']
    newVenue.venueState = request.POST['state']
    newVenue.venueAddress = request.POST['venueaddress']
    newVenue.venueContactCountryCode = request.POST['venuecontactcountrycode']
    newVenue.venueContactNumber = request.POST['venuecontactnumber']
    newVenue.venueEmail = request.POST['venueemail']
    newVenue.venueCapacity = request.POST['venuecapacity']
    newVenue.venueImage = request.FILES['venueimage']
    newVenue.venuePrice = float(request.POST['venueprice'])
    newVenue.venueRating = float(request.POST['venuerating'])
    newVenue.save()
    return HttpResponseRedirect("http://localhost:8000/administrator/viewallvenue/")

@login_required_1
def viewAllVenue(request):
    allVenues = venueModel.venueTable.objects.all()
    context = {'allvenues':allVenues}
    res = render(request,'administrator/viewAllVenue.html',context)
    return HttpResponse(res)


def showEditVenuePage(request, venue_id):
    venueTobeEdited = venueModel.venueTable.objects.get(venueId=venue_id)
    context = {'venue':venueTobeEdited}
    res = render(request, 'administrator/editVenuePage.html',context)
    return HttpResponse(res)

@login_required_1
def updateVenue(request):
    updatedVenue = venueModel.venueTable()
    updatedVenue.venueId = request.POST['venueid']
    updatedVenue.venueName = request.POST['venuename']
    updatedVenue.venueDescription = request.POST['venuedescription']
    updatedVenue.venueCity = request.POST['city']
    updatedVenue.venueState = request.POST['state']
    updatedVenue.venueAddress = request.POST['venueaddress']
    updatedVenue.venueContactCountryCode = request.POST['venuecontactcountrycode']
    updatedVenue.venueContactNumber = request.POST['venuecontactnumber']
    updatedVenue.venueEmail = request.POST['venueemail']
    updatedVenue.venueCapacity = request.POST['venuecapacity']
    try:
        if request.FILES['venueimage']:
            updatedVenue.venueImage = request.FILES['venueimage']
    except:
        updatedVenue.venueImage = request.POST['previousvenueimage']
    updatedVenue.venuePrice = request.POST['venueprice']
    updatedVenue.venueRating = request.POST['venuerating']
    updatedVenue.save()
    return HttpResponseRedirect("http://localhost:8000/administrator/viewallvenue/")

def deleteVenue(request, venue_id):
    venueTobeDeleted = venueModel.venueTable.objects.get(venueId=venue_id)
    venueTobeDeleted.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def viewAllBooking(request):
    allBookings = bookingModel.bookingTable.objects.all()
    context = {'allbookings':allBookings}
    res = render(request, 'administrator/viewAllBooking.html', context)
    return HttpResponse(res)

@login_required_1
def showAddFoodForm(request):
    res = render(request, 'administrator/addFoodForm.html')
    return HttpResponse(res)

@login_required_1
def addFood(request):
    newFood = bookingModel.foodTable()
    try:
        if request.FILES['foodimage']:
            newFood.foodImage = request.FILES['foodimage']
    except:
        newFood.foodImage = 'media/addFood.png' 
    newFood.foodName = request.POST['foodname']
    newFood.foodCuisine = request.POST['foodcuisine']
    newFood.foodPricePerServing = float(request.POST['foodpriceperserving'])
    newFood.foodCode = request.POST['foodcode'].upper()
    try:
        foodAlreadyExist = bookingModel.foodTable.objects.get(foodName = newFood.foodName)
        if foodAlreadyExist:
            context = {'newFood':newFood,
                       'food_Name_Error':"***Food name already exists."}
            res = render(request, 'administrator/addFoodForm.html', context)
            return HttpResponse(res)
    except:
        try:
            foodAlreadyExist = bookingModel.foodTable.objects.get(foodCode = newFood.foodCode)
            if foodAlreadyExist:
                context = {'newFood':newFood,
                       'food_Code_Error':"***Food code already exists."}
                res = render(request, 'administrator/addFoodForm.html', context)
                return HttpResponse(res)
        except:
            pass
    newFood.save()
    return HttpResponseRedirect("http://localhost:8000/administrator/viewallfood/")

def editFoodDetails(request, food_id):
    foodToBeEdited = bookingModel.foodTable.objects.get(foodId = food_id)
    context = {'food':foodToBeEdited}
    res = render(request, 'administrator/editFoodPage.html', context)
    return HttpResponse(res)

@login_required_1
def updateFoodDetails(request):
    updatedFood = bookingModel.foodTable()
    foodToBeEdited = bookingModel.foodTable.objects.get(foodId = request.POST['foodid'])
    try:
        if request.FILES['foodimage']:
            updatedFood.foodImage = request.FILES['foodimage']
    except:
        updatedFood.foodImage = request.POST['previousfoodimage'] 
    updatedFood.foodId = request.POST['foodid']
    updatedFood.foodName = request.POST['foodname']
    updatedFood.foodCuisine = request.POST['foodcuisine']
    updatedFood.foodPricePerServing = float(request.POST['foodpriceperserving'])
    updatedFood.foodCode = request.POST['foodcode'].upper()
    try:
        allFoodList = bookingModel.foodTable.objects.exclude(foodId = updatedFood.foodId)
        for food in allFoodList:
            if food.foodName == updatedFood.foodName:
                context = {'updatedFood':updatedFood,
                           'food':foodToBeEdited,
                       'food_Name_Error':"***Food name already exists."}
                res = render(request, 'administrator/editFoodPage.html', context)
                return HttpResponse(res)
    except:
        pass
    try:
        for food in allFoodList:
            if food.foodCode == updatedFood.foodCode:
                context = {'updatedFood':updatedFood,
                           'food':foodToBeEdited,
                           'food_Code_Error':"***Food code already exists."}
                res = render(request, 'administrator/editFoodPage.html', context)
                return HttpResponse(res)
    except:
        pass
    updatedFood.save()
    return HttpResponseRedirect("http://localhost:8000/administrator/viewallfood/")
    
def deleteFood(request, food_id):
    foodToBeDeleted = bookingModel.foodTable.objects.get(foodId = food_id)
    foodToBeDeleted.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def viewAllFood(request):
    allFoods = bookingModel.foodTable.objects.all()
    context = {'allfoods':allFoods}
    res = render(request, 'administrator/viewAllFood.html', context)
    return HttpResponse(res)

@login_required_1
def showAddDanceFloorForm(request):
    res = render(request, 'administrator/addDanceFloorForm.html')
    return HttpResponse(res)

@login_required_1
def addDanceFloor(request):
    newDanceFloor = bookingModel.danceFloorTable()
    try:
        if request.FILES['dancefloorimage']:
            newDanceFloor.danceFloorImage = request.FILES['dancefloorimage']
    except:
        newDanceFloor.danceFloorImage = 'media/danceFloorIcon.jpg' 
    newDanceFloor.danceFloorType = request.POST['dancefloortype']
    newDanceFloor.danceFloorDescription = request.POST['dancefloordescription']
    newDanceFloor.danceFloorPricePerBooking = float(request.POST['dancefloorpriceperbooking'])
    newDanceFloor.danceFloorCode = request.POST['dancefloorcode'].upper()
    try:
        danceFloorAlreadyExist = bookingModel.danceFloorTable.objects.get(danceFloorCode=newDanceFloor.danceFloorCode)
        if danceFloorAlreadyExist:
            context = {'newDanceFloor':newDanceFloor,
                       'dancefloor_Code_Error':"***Dance floor code already exists."}
            res = render(request, 'administrator/addDanceFloorForm.html', context)
            return HttpResponse(res)
    except:
        pass
    newDanceFloor.save()
    return HttpResponseRedirect("http://localhost:8000/administrator/viewalldancefloor/")

def showEditDanceFloorPage(request, dancefloor_id):
    danceFloorToBeEdited = bookingModel.danceFloorTable.objects.get(danceFloorId = dancefloor_id)
    context = {'dancefloor':danceFloorToBeEdited}
    res = render(request, 'administrator/editDanceFloorPage.html', context)
    return HttpResponse(res)

@login_required_1
def updateDanceFloorDetails(request):
    updatedDanceFloor = bookingModel.danceFloorTable()
    danceFloorToBeEdited = bookingModel.danceFloorTable.objects.get(danceFloorId = int(request.POST['dancefloorid']) )
    try:
        if request.FILES['dancefloorimage']:
            updatedDanceFloor.danceFloorImage = request.FILES['dancefloorimage']
    except:
        updatedDanceFloor.danceFloorImage = request.POST['olddancefloorimage'] 
    updatedDanceFloor.danceFloorId = request.POST['dancefloorid']
    updatedDanceFloor.danceFloorType = request.POST['dancefloortype']
    updatedDanceFloor.danceFloorDescription = request.POST['dancefloordescription']
    updatedDanceFloor.danceFloorPricePerBooking = request.POST['dancefloorpriceperbooking']
    updatedDanceFloor.danceFloorCode = request.POST['dancefloorcode'].upper()
    try:
        allDanceFloorList = bookingModel.danceFloorTable.objects.exclude(danceFloorId = updatedDanceFloor.danceFloorId)
        for dancefloor in allDanceFloorList:
            if dancefloor.danceFloorCode == updatedDanceFloor.danceFloorCode:
                context = {'updatedDanceFloor':updatedDanceFloor,
                           'dancefloor':danceFloorToBeEdited,
                       'dancefloor_Code_Error':"***Dance floor code already exists."}
                res = render(request, 'administrator/editDanceFloorPage.html', context)
                return HttpResponse(res)
    except:
        pass
    updatedDanceFloor.save()
    return HttpResponseRedirect("http://localhost:8000/administrator/viewalldancefloor/")

def deleteDanceFloor(request, dancefloor_id):
    danceFloorToBeDeleted = bookingModel.danceFloorTable.objects.get(danceFloorId=dancefloor_id)
    danceFloorToBeDeleted.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required_1
def viewAllDanceFloor(request):
    allDanceFloors = bookingModel.danceFloorTable.objects.all()
    context = {'alldancefloors':allDanceFloors}
    res = render(request, 'administrator/viewAllDanceFloor.html',context)
    return HttpResponse(res)

@login_required_1
def viewAllPayment(request):
    allPayments = paymentModel.paymentTable.objects.all()
    context = {'allpayments':allPayments}
    res = render(request,'administrator/viewAllPayment.html',context)
    return HttpResponse(res)

@login_required_1
def viewAllInvoice(request):
    allInvoices = invoiceModel.invoiceTable.objects.all()
    context = {'allinvoices':allInvoices}
    res = render(request,'administrator/viewAllInvoice.html',context)
    return HttpResponse(res)

@login_required_1
def viewAllFeedback(request):
    allFeedbacks = customerModel.feedbackTable.objects.all()
    context = {'allfeedbacks': allFeedbacks}
    res = render(request,'administrator/viewAllFeedback.html',context)
    return HttpResponse(res)

def feedbackResponseForm(request, feedback_id):
    feedbackToBeResponded = customerModel.feedbackTable.objects.get(feedbackId = feedback_id)
    context = {'feedback':feedbackToBeResponded}
    response = render(request, 'administrator/feedbackResponseForm.html', context)
    return HttpResponse(response)

@login_required_1
def submitFeedbackResponse(request):
    updatedFeedback = customerModel.feedbackTable()
    currentCustomer = customerModel.customerTable.objects.get(customerId = int(request.POST['customerid']))
    updatedFeedback.feedbackId = request.POST['feedbackid']
    updatedFeedback.customerId = currentCustomer
    updatedFeedback.feedbackType = request.POST['feedbacktype']
    updatedFeedback.feedbackDescription = request.POST['feedbackdescription']
    updatedFeedback.feedbackResponse = request.POST['feedbackresponse']
    updatedFeedback.feedbackStatus = request.POST['feedbackstatus']
    updatedFeedback.save()
    return HttpResponseRedirect('http://localhost:8000/administrator/viewallfeedback/')

@login_required_1
def showAccountDetails(request):
    username = request.session['adminUsername']
    currentAdmin = adminModel.administratorTable.objects.get(adminUsername = username)
    context = {'admin':currentAdmin}
    res = render(request, 'administrator/myAccountPage.html',context)
    return HttpResponse(res)

@login_required_1
def saveAccountDetails(request):
    updatedAdmin = adminModel.administratorTable()
    adminList = adminModel.administratorTable()
    updatedAdmin.adminId = request.POST['adminid']
    updatedAdmin.adminName = request.POST['adminname']
    try:
        if request.FILES['adminprofileimage']:
            updatedAdmin.adminImage = request.FILES['adminprofileimage']
    except:
        updatedAdmin.adminImage = request.POST['previousprofileimage']
    try:
        if request.POST['admingender']:
            updatedAdmin.adminGender = request.POST['admingender']
    except:
        updatedAdmin.adminGender = request.POST['previousgendervalue']
    
    newDateOfBirth = request.POST['admindob']
    if newDateOfBirth:
        updatedAdmin.adminDob = request.POST['admindob']
    else:
        updatedAdmin.adminDob = request.POST['previousdobdate']

    updatedAdmin.adminDesignation = request.POST['admindesignation']    
    updatedAdmin.adminEmail = request.POST['adminemail']
    updatedAdmin.adminMobileCountryCode =  request.POST['adminmobilecountrycode']
    updatedAdmin.adminMobileNumber = request.POST['adminmobilenumber']
    updatedAdmin.adminAddress = request.POST['adminaddress']
    updatedAdmin.adminUsername = request.POST['adminusername']
    updatedAdmin.adminPassword = request.POST['adminpassword']
    context = {'admin':updatedAdmin}
    flag = 0
    try:
        adminList = adminModel.administratorTable.objects.exclude(adminId = updatedAdmin.adminId)
        for adminX in adminList:
            if adminX.adminEmail == updatedAdmin.adminEmail:
                context['email_error'] = "***Email id already registered."
                flag = 1
                break
    except:
        pass
    try:
        adminList = adminModel.administratorTable.objects.exclude(adminId = updatedAdmin.adminId)
        for adminY in adminList:
            if adminY.adminMobileNumber == updatedAdmin.adminMobileNumber:
                context['mobile_error'] = "***Mobile number already registered."
                flag = 1
                break
    except:
        pass
    try:
        adminList = adminModel.administratorTable.objects.exclude(adminId = updatedAdmin.adminId)
        for adminZ in adminList:
            if adminZ.adminUsername == updatedAdmin.adminUsername:
                context['username_error'] = "***Username already taken."
                flag = 1
                break
    except:
        pass
    if flag == 1:
        response = render(request, 'administrator/myAccountPage.html', context)
        return HttpResponse(response)            
    updatedAdmin.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))