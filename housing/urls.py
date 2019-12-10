from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *


app_name = 'housing'

urlpatterns = [
    path('category/', RentalCategoryListView.as_view(), name='category-list'),
    path('category/new/', RentalCategoryCreateView.as_view(), name='category-create'),
    path('category/<slug>/', RentalCategoryDetailView.as_view(), name='category-detail'),
    path('category/<slug>/edit/', RentalCategoryUpdateView.as_view(), name='address-edit'),
    path('category/<slug>/detete/', RentalCategoryDeleteView.as_view(),name='category-remove'),
    # path('property/', RentalPropertyListCreateView.as_view()),
    # path('property/<int:pk>/', RentalPropertyRUDView.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
