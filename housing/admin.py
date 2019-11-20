from django.contrib import admin

from .models import HousingCategory, RentalProperty
# Register your models here.

class HousingCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

class RentalProperty(admin.ModelAdmin):
    list_display = ["name","propertyType","price"]
    list_filter =['properyType']
