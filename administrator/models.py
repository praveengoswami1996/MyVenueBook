from django.db import models

#admin Model
class administratorTable(models.Model):
    adminId = models.AutoField(primary_key=True)
    adminName = models.CharField(max_length=50)
    adminDob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    adminGender = models.CharField(max_length=15)
    adminDesignation = models.CharField(max_length=50) 
    adminEmail = models.EmailField(max_length=100)
    adminMobileCountryCode = models.CharField(max_length=10, default='')
    adminMobileNumber = models.CharField(max_length=20)
    adminAddress = models.CharField(max_length=120)
    adminImage = models.ImageField(upload_to='media/', default='', blank=True)
    adminUsername = models.CharField(max_length=50)
    adminPassword = models.CharField(max_length=50)

class messageTable(models.Model):
    messageId = models.AutoField(primary_key=True)
    messageDate = models.DateField(auto_now_add=True)
    senderName = models.CharField(max_length=50)
    senderEmail = models.EmailField(max_length=100)
    messageStatus = models.CharField(max_length=50)
    senderMessage = models.TextField()

    