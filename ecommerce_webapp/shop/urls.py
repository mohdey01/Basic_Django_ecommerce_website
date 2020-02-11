from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Index,name='ShopIndex'),
    path('about/', views.AboutUs,name='AboutUs'),
    path('contact/', views.ContactUs,name='ContactUs'),
    path('tracker/', views.TrackingStatus,name='TrackingStatus'),
    path('search/', views.searchProducts,name='searchProducts'),
   path('productview/<int:myid>', views.ProductView,name='ProductView'),
   path('checkout/', views.CheckOut,name='CheckOut'),
    
]
