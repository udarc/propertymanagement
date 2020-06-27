
from django import forms
from .models import RentalProperty
class RentalPropertyForm(forms.ModelForm):
    # photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), max_length=120,allow_empty_file=True)
    photos = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))
    class Meta:
        model = RentalProperty
        fields = ['name', 'location','propertyType','rooms', 'size','photos', 'amenities', 'price']