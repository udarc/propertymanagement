from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *


app_name = 'housing'

urlpatterns = [
    path('categories/', RentalCategoryListView.as_view(), name='category-list'),
    path('category/new/', RentalCategoryCreateView.as_view(), name='category-create'),
    path('category/<slug>/', RentalCategoryDetailView.as_view(), name='category-detail'),
    path('category/<slug>/edit/', RentalCategoryUpdateView.as_view(), name='category-edit'),
    path('category/<slug>/detete/', RentalCategoryDeleteView.as_view(),name='category-remove'),
    
    path('properies/', RentalPropertyListView.as_view(), name='property-list'),
    path('property/add/', RentalPropertyCreateView.as_view(), name='property-create'),
    path('property/<int:pk>/', RentalPropertyDetailView.as_view(), name='property-detail'),
    path('property/<int:pk>/edit/', RentalPropertyUpdateView.as_view(), name='property-edit'),
    path('property/<int:pk>/delete/', RentalPropertyDeleteView.as_view(), name='property-remove'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
