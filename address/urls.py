from django.urls import path,include   
from rest_framework import routers 
from .views import *

app_name = "address"

urlpatterns  = [
    path('', AddressListView.as_view(), name='address-list'),
    path('add/', AddressCreateView.as_view(), name='address-add'),
    path('<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('<int:pk>/edit/', AddressUpdateView.as_view(), name='address-edit'),
    path('<int:pk>/remove/', AddressDeleteView.as_view(), name='address-remove'),
]
