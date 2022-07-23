from django.urls import path
from customer import views


urlpatterns = [
    path('loginform/', views.customerLoginForm),
    path('signupform/', views.customerSignupForm),
    path('donewregistration/', views.customerNewRegistration),
    path('dologinvalidate/', views.customerLoginValidate),
    path('deletemyaccount/', views.deleteMyAccount),
    path('dashboard/', views.customerDashboard),
    path('bookingrecords/', views.customerBookingRecords),
    path('searchvenuebystate/', views.searchVenueByState),
    path('showallvenuelist/', views.showAllVenueList),
    path('feedbackform/', views.customerFeedbackForm),
    path('submitfeedback/', views.submitFeedback),
    path('myprofile/', views.myProfile),
    path('saveprofile/', views.saveCustomerProfile),
    path('myinvoices/', views.myInvoices),
    path('myfeedbacks/', views.myFeedbacks),
    path('logout/', views.customerLogout),
]