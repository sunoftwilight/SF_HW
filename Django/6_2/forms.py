from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()

    class Meta:
        model = Reservation
        fields = '__all__'