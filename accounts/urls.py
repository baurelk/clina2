from django.urls import path
from accounts import views
urlpatterns = [
    
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.logoutView.as_view(), name='logout'),

]
