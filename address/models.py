from django.db import models

# Create your models here.
class Address(models.Model):
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=60, default="Madison")
    state = models.CharField(max_length=30, default="WI")
    zipcode = models.CharField(max_length=10, default="53703")
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'