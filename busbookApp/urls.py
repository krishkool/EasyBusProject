from django.urls.resolvers import URLPattern
from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name= 'home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/sign_up/', views.signup_view, name = 'signup'),
    path('customer',views.custDash, name = 'customerpage'),
    path('customerprofile', views.custProfile, name= 'customerprofile'),
    path('customerprofiledata',views.customerCreateProfile),
    path('logout', views.logout_view, name='logout'),
    path('bookingpage', views.bookingPage, name= 'ticketbooking'),
    path('busbooksearch', views.searchBus),
    path('booktickets', views.bookTicket)

] 
