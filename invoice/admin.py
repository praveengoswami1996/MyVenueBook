from django.contrib import admin
from invoice.models import invoiceTable

# Register your models here.

class invoiceTableAdmin(admin.ModelAdmin):
    list_display = ['invoiceId', 'bookingId', 'customerId','invoiceTotalAmount','invoiceDate',]
    
admin.site.register(invoiceTable, invoiceTableAdmin)
