from django.contrib import admin
from customer.models import customerTable, feedbackTable

# Register your models here.

class customerTableAdmin(admin.ModelAdmin):
    list_display = ['customerId', 'customerName', 'customerEmail','customerMobileNumber','customerUsername']

class feedbackTableAdmin(admin.ModelAdmin):
    list_display = ['feedbackId', 'customerId', 'feedbackType','feedbackDescription','feedbackResponse', 'feedbackStatus']
    
admin.site.register(customerTable, customerTableAdmin)
admin.site.register(feedbackTable, feedbackTableAdmin)