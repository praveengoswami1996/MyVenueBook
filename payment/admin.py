from django.contrib import admin
from payment.models import paymentTable, allStatusTable

# Register your models here.
class paymentTableAdmin(admin.ModelAdmin):
    list_display = ['paymentId', 'bookingId', 'paymentAmount', 'paymentDate','paymentTime','paymentMode','paymentStatus']

class allStatusTableAdmin(admin.ModelAdmin):
    list_display = ['id','customerId','bookingId','paymentId','bookingStatus','paymentStatus']   

admin.site.register(paymentTable, paymentTableAdmin)
admin.site.register(allStatusTable, allStatusTableAdmin)
