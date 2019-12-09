from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import date

class TimestampModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
def avatar_path(instance, filename):
    return "user_{id}/{file}".format(id=instance.user.id, file=filename)

class UserProfile(TimestampModel):
    GENDER_CHOICES = [('M', 'Male'),
                      ('F', 'Female')]
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    biography = models.TextField()
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    avatar = models.ImageField(
        upload_to='uploads/avatars', default='', blank=True)
    profession = models.CharField(max_length=100, blank=True, null=True)

    @property
    def age(self):
        today = date.today()
        if not self.birthday:
            self.birthday = today
        delta = (today.year - self.birthday.year) - ((today.month,
                                                      today.day) < (self.birthday.month, self.birthday.day))
        return delta

    def __str__(self):
        return '{}'.format(self.user)

    def get_absolute_url(self):
        return reverse('accounts:profile', {'slug': self.user.username})


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
