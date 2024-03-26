from django.urls import path
from app import views
urlpatterns = [
    
    path('', views.dashbordView, name='home'),
    path('/add/customer', views.AddCustomer, name='add_customer'),

]
