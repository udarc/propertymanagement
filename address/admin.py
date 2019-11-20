from django.contrib import admin
from address.models import Address
# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street_address1',"city",'state']

admin.site.register(Address,AddressAdmin)