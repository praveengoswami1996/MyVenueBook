from django.db import models
from django.utils import timezone
from customer.models import customerTable
from venue.models import venueTable

class bookingTable(models.Model):
    bookingId = models.AutoField(primary_key=True) 
    customerId = models.ForeignKey(customerTable, on_delete=models.CASCADE)
    venueId = models.ForeignKey(venueTable, on_delete=models.CASCADE)
    eventType = models.CharField(max_length=150, default='')
    bookingDateTime = models.DateTimeField(default=timezone.now)
    bookingStartDate = models.DateField()
    bookingEndDate = models.DateField()
    bookingDays = models.IntegerField()
    bookingStatus = models.CharField(max_length=50, blank=True)

#Food Table
class foodTable(models.Model):
    foodId = models.AutoField(primary_key=True)
    foodName = models.CharField(max_length=50)
    foodImage = models.ImageField(upload_to='media/', default='', blank=True) 
    foodCuisine = models.CharField(max_length=50)
    foodPricePerServing = models.FloatField()
    foodCode = models.CharField(max_length=50)

#DJ Table
class danceFloorTable(models.Model):
    danceFloorId = models.AutoField(primary_key=True)
    danceFloorType = models.CharField(max_length=50)
    danceFloorDescription = models.CharField(max_length=250, default='')
    danceFloorImage = models.ImageField(upload_to='media/', default='', blank=True) 
    danceFloorPricePerBooking = models.FloatField()
    danceFloorCode = models.CharField(max_length=50)

class customerFoodTable(models.Model):
    bookingId = models.ForeignKey(bookingTable, on_delete=models.CASCADE)
    foodId = models.ForeignKey(foodTable, on_delete=models.CASCADE)

class customerDanceFloorTable(models.Model):
    bookingId = models.ForeignKey(bookingTable, on_delete=models.CASCADE)
    danceFloorId = models.ForeignKey(danceFloorTable, on_delete=models.CASCADE)