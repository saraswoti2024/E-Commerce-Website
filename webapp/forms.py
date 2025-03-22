from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ContactForms(forms.Form):
    email = forms.EmailField()
    phonenumber = PhoneNumberField(widget=forms.TextInput(attrs={'id': 'phone'}))
    address = forms.CharField(max_length=200)
    message = forms.CharField()
