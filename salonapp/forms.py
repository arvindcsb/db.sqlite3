from django import forms
from salonapp.models import Salons
from customerapp.models import Booking,Rating


class SalonsForm(forms.ModelForm):
    class Meta:
        model=Salons
        fields="__all__"