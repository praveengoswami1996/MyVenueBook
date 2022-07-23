from django.db import models
from booking.models import bookingTable
from customer.models import customerTable 

# Create your models here.

class paymentTable(models.Model):
    paymentId = models.AutoField(primary_key=True)
    bookingId = models.ForeignKey(bookingTable, on_delete=models.CASCADE)
    paymentAmount = models.FloatField()
    paymentDate = models.DateField(auto_now_add=True)
    paymentTime = models.TimeField(auto_now_add=True) 
    paymentMode = models.CharField(max_length=50)
    paymentStatus = models.CharField(max_length=50)
    cardNumber = models.BigIntegerField()
    cardExpiryMonth = models.IntegerField()
    cardExpiryYear = models.IntegerField()
    cvvNumber = models.IntegerField()
    nameOnCard = models.CharField(max_length=50)

class allStatusTable(models.Model):
    customerId = models.ForeignKey(customerTable, on_delete=models.CASCADE)
    bookingId = models.ForeignKey(bookingTable, on_delete=models.CASCADE)
    paymentId = models.ForeignKey(paymentTable, on_delete=models.CASCADE, null=True, blank=True)
    paymentStatus = models.CharField(max_length=20)
    bookingStatus = models.CharField(max_length=20)