from django.db import models

# Create your models here.
class HousingCategory(models.Model):
    name = models.CharField(max_length= 80, unique=True)
    slug = models.SlugField(max_length=80)
    summary = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class RentalProperty(models.Model):
    name = models.CharField(max_length= 150)
    location = models.ForeignKey('Address')
    slug = models.SlugField()
    propertyType = models.ForeignKey("HousingCategory")
    rooms = models.IntegerField(default=1)
    photos = models.ImageField(upload_to="uploads")
    size = models.FloatField(blank=True, null=True)
    amenities = models.TextField()
    price = models.DecimalField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)





    
