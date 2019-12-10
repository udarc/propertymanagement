from django.db import models
from accounts.models import UserProfile, TimestampModel

from django.urls import reverse

# Create your models here.
class Address(TimestampModel):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=60, default="Madison")
    state = models.CharField(max_length=30, default="WI")
    zipcode = models.CharField(max_length=10, default="53703")
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return '%s %s %s' % (self.street_address1, self.city, self.state)

    def get_absolute_url(self):
        return reverse('address:address-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('address:address-edit', args=[self.pk])

    def get_delete_url(self):
        return reverse('address:address-remove', kwargs={'pk': self.pk})