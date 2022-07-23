from django.db import models
from booking.models import bookingTable
from customer.models import customerTable

# Create your models here.
class invoiceTable(models.Model):
    invoiceId = models.AutoField(primary_key=True)
    bookingId = models.ForeignKey(bookingTable, on_delete=models.CASCADE)
    customerId = models.ForeignKey(customerTable, on_delete=models.CASCADE)
    invoiceName = models.CharField(max_length=50)
    invoiceAddress = models.CharField(max_length=120)
    invoiceCity = models.CharField(max_length=50)
    invoiceState = models.CharField(max_length=50)
    invoicePincode = models.CharField(max_length=20)
    venueParticular = models.CharField(max_length=250)
    foodParticular = models.CharField(max_length=250)     
    danceFloorParticular = models.CharField(max_length=250)
    venueParticularAmount = models.FloatField()
    foodParticularAmount = models.FloatField()
    danceFloorParticularAmount = models.FloatField()
    invoiceTotalAmount = models.FloatField()
    invoiceDate = models.DateField(auto_now_add=True)

