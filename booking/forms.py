from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ReservationForm(forms.Form):
    ## location
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(min_length=10,max_length=10)


