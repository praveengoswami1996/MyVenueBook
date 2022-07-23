from django.db import models

#Venue Table
class venueTable(models.Model):
    venueId = models.AutoField(primary_key=True)
    venueName = models.CharField(max_length=100)
    venueDescription = models.TextField()
    venueCity = models.CharField(max_length=50) 
    venueState = models.CharField(max_length=50)
    venueAddress = models.CharField(max_length=120)
    venueContactCountryCode = models.CharField(max_length=10, default='')
    venueContactNumber = models.CharField(max_length=20, default='')
    venueEmail = models.EmailField(max_length=100)
    venueCapacity = models.IntegerField()
    venueImage = models.ImageField(upload_to='media/', default='')
    venuePrice = models.FloatField() 
    venueRating = models.FloatField()
