from django import forms
from adminsapp.models import Admins
from customerapp.models import Customer,Booking,Rating
from salonapp.models import Salons

class AdminsForm(forms.ModelForm):
    class Meta:
        model=Admins
        fields="__all__"