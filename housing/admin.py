from django.contrib import admin

from .models import RentalCategory, RentalProperty
# Register your models here.

class RentalCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {'slug': ('title',)}

class RentalPropertyAdmin(admin.ModelAdmin):
    list_display = ["name","propertyType","price"]
    list_filter =['propertyType']
admin.site.register(RentalCategory, RentalCategoryAdmin)
admin.site.register(RentalProperty, RentalPropertyAdmin)