from django.urls import path
from app_params import views
urlpatterns = [
    
    path('clothing/category/', views.clothingCatPage, name='clothing_cat_page'),

]
