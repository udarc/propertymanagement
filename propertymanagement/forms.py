from django import forms

class ContactForm(forms.Form):
    name =  forms.CharField(required = True)
    sender_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)