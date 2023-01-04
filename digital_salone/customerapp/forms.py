from django import forms
from customerapp.models import Contact,Customer,Booking,Rating
from salonapp.models import Salons

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields="__all__"
