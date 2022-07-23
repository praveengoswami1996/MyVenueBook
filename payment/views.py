import datetime
from django.shortcuts import render
import pytz
from django.http import HttpResponse, HttpResponseRedirect
from booking import models as bookingModel
from customer import models as customerModel
from invoice import models as invoiceModel
from payment import models as paymentModel
from venue import models as venueModel

# Create your views here.
def makePaymentAndCreateInvoice(request, booking_id, customer_id):
    customerInvoice = invoiceModel.invoiceTable()
    customerPayment = paymentModel.paymentTable()
    allStatus = paymentModel.allStatusTable()
    currentBooking = bookingModel.bookingTable.objects.get(bookingId=booking_id)
    currentCustomer = customerModel.customerTable.objects.get(customerId=customer_id)
    
    customerPayment.bookingId = currentBooking
    customerPayment.paymentAmount = float(request.POST['amountpayable'])
    customerPayment.paymentMode = request.POST['paymentmode']
    customerPayment.paymentStatus = request.POST['paymentstatus']
    customerPayment.cardNumber = request.POST['cardnumber']
    customerPayment.cardExpiryMonth = request.POST['expirymonth']
    customerPayment.cardExpiryYear = request.POST['expiryyear']
    customerPayment.cvvNumber = request.POST['cvvnumber']
    customerPayment.nameOnCard = request.POST['cardholdername']
    try:
        alreadyPaid = paymentModel.paymentTable.objects.get(bookingId = currentBooking)
        if alreadyPaid:
            context = {'payment':alreadyPaid}
            response = render(request, 'payment/paymentReceiptPage.html', context)
            return HttpResponse(response) 
    except:
        pass
    customerPayment.save()
    #Updating All Status Table
    allStatus.id = int(request.POST['allstatusid']) 
    allStatus.customerId = currentCustomer
    allStatus.bookingId = currentBooking
    allStatus.paymentId = customerPayment
    allStatus.bookingStatus = "Booked"
    allStatus.paymentStatus = "Paid"
    allStatus.save()
    #Creating Invoice
    customerInvoice.bookingId = currentBooking
    customerInvoice.customerId = currentCustomer
    customerInvoice.invoiceName = request.POST['fullname']
    customerInvoice.invoiceAddress = request.POST['billingaddress']
    customerInvoice.invoiceCity = request.POST['city']
    customerInvoice.invoiceState = request.POST['state']
    customerInvoice.invoicePincode = request.POST['pincode']
    customerInvoice.venueParticular = request.POST['venueparticular']
    customerInvoice.foodParticular = request.POST['foodparticular']
    customerInvoice.danceFloorParticular = request.POST['dancefloorparticular']
    customerInvoice.venueParticularAmount = float(request.POST['venueparticularcharge'])
    customerInvoice.foodParticularAmount = float(request.POST['foodparticularcharge'])
    customerInvoice.danceFloorParticularAmount = float(request.POST['dancefloorparticularcharge'])
    customerInvoice.invoiceTotalAmount = float(request.POST['amountpayable'])
    customerInvoice.save()
    context = {'payment':customerPayment}
    response = render(request, 'payment/paymentReceiptPage.html', context)
    return HttpResponse(response)
    
def paymentProcess(request, booking_id):
    currentBooking = bookingModel.bookingTable.objects.get(bookingId=booking_id)
    allStatus = paymentModel.allStatusTable.objects.get(bookingId=currentBooking)
    venueBookingCharge = float(request.POST['venuebookingcharge'])
    addOnFoodCharge = float(request.POST['addonfoodcharge'])
    addOnDanceFloorCharge = float(request.POST['addondancefloorcharge'])
    amountPayable = float(request.POST['amountpayable'])
    context = {'venueBookingCharge':venueBookingCharge,
               'addOnFoodCharge':addOnFoodCharge,
               'addOnDanceFloorCharge':addOnDanceFloorCharge,
               'amountPayable':amountPayable,
               'booking_details':currentBooking,
               'allStatus':allStatus}
    res = render(request,'payment/paymentFormPageWithOrderSummary.html',context)
    return HttpResponse(res)
    
def createBillForPayment(request, booking_id):
    addOnFood = bookingModel.customerFoodTable.objects.all().filter(bookingId=booking_id)
    addOnFloor = bookingModel.customerDanceFloorTable.objects.all().filter(bookingId=booking_id)
    currentBooking = bookingModel.bookingTable.objects.get(bookingId=booking_id)
    context = {'booking_details':currentBooking,
               'addOnFoods':addOnFood,
               'addOnFloors':addOnFloor}
    res = render(request,'payment/billingPageWithBookingDetails.html', context)
    return HttpResponse(res)

def removeFoodItemFromBilling(request, food_id, booking_id):
    D = request.session['foodid']
    D.remove(str(food_id))
    request.session['foodid'] = D
    foodToRemove = bookingModel.customerFoodTable.objects.get(foodId=food_id, bookingId=booking_id)
    foodToRemove.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removeDanceFloorFromBilling(request, dancefloor_id, booking_id):
    D = request.session['dancefloorid']
    D.remove(str(dancefloor_id))
    request.session['dancefloorid'] = D
    danceFloorToRemove = bookingModel.customerDanceFloorTable.objects.get(danceFloorId=dancefloor_id, bookingId=booking_id)
    danceFloorToRemove.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))