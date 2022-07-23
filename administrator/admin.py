from django.contrib import admin
from administrator.models import administratorTable, messageTable

# Register your models here.
class administratorTableAdmin(admin.ModelAdmin):
    list_display = ['adminId','adminName','adminGender','adminDesignation','adminUsername','adminPassword']

class messageTableAdmin(admin.ModelAdmin):
    list_display = ['messageId','senderName','senderEmail','senderMessage','messageStatus']

admin.site.register(administratorTable, administratorTableAdmin)
admin.site.register(messageTable, messageTableAdmin)