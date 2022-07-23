from django.db import models
# Create your models here.
#Customer Model
class customerTable(models.Model):
    customerId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=50)
    customerImage = models.ImageField(upload_to='media/', default='', blank=True) 
    customerDob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    customerGender = models.CharField(max_length=15) 
    customerEmail = models.EmailField(max_length=100)
    customerMobileCountryCode = models.CharField(max_length=10, default='')
    customerMobileNumber = models.CharField(max_length=20)
    customerAddress = models.CharField(max_length=120)
    customerCity = models.CharField(max_length=50,default='')
    customerState = models.CharField(max_length=50,default='')
    customerPincode = models.CharField(max_length=20,default='') 
    customerUsername = models.CharField(max_length=50)
    customerPassword = models.CharField(max_length=50)

class feedbackTable(models.Model):
    feedbackId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(customerTable, on_delete=models.CASCADE)
    feedbackType = models.CharField(max_length=20)
    feedbackDescription = models.TextField()
    feedbackResponse = models.TextField(blank=True)
    feedbackStatus = models.CharField(max_length=20) 


