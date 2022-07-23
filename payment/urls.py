from django.urls import path
from payment import views

urlpatterns = [
    path('makepayment/<int:booking_id>/<int:customer_id>/',views.makePaymentAndCreateInvoice),
    path('paymentprocess/<int:booking_id>/',views.paymentProcess),
    path('billingprocess/<int:booking_id>/',views.createBillForPayment),
    path('removefooditem/<int:food_id>/<int:booking_id>/', views.removeFoodItemFromBilling),
    path('removedancefloor/<int:dancefloor_id>/<int:booking_id>/', views.removeDanceFloorFromBilling)
]