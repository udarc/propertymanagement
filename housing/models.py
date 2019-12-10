from django.db import models
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from accounts.models import UserProfile
from django.urls import reverse


import os
from address.models import Address


def change_slugify_delimiter(content):
    return content.replace('_', '-').lower()


def get_upload_path(instance, filename):
    upload_dir = os.path.join('uploads',instance.rentalslug)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

# Create your models here.
class RentalCategory(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length= 80, unique=True)
    slug = models.SlugField(max_length= 80, default=slugify(title),unique=True)
    # catslug = AutoSlugField(populate_from="title",slugify_function=change_slugify_delimiter)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def save(self, *args,**kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)        
    #     return super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('housing:category-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('housing:category-edit', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('housing:category-remove', kwargs={'slug': self.slug})


class RentalProperty(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length= 150)
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    propertyType = models.ForeignKey(RentalCategory, on_delete=models.SET_DEFAULT,default="Rental property")
    rentalslug = AutoSlugField(populate_from=["location","name"],slugify_function=change_slugify_delimiter)   
    rooms = models.IntegerField(default=1)
    # photos = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    size = models.FloatField(blank=True, null=True)
    amenities = models.TextField()
    price = models.DecimalField(decimal_places=3,max_digits=4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


   # https://stackoverflow.com/questions/49929620/uploading-multiple-images-in-django-with-django-multiupload-library

class Image(models.Model):
    rentalProperty = models.ForeignKey(RentalProperty, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to=get_upload_path)



# //https://stackoverflow.com/questions/49827112/how-to-upload-multiple-images-from-a-single-choose-files-selector-in-django-ad
# https://stackoverflow.com/questions/5135556/dynamic-file-path-in-django

    
