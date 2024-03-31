from django import forms
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('created_at', 'customer',)
# add date picker
        widgets = {
            'booking_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
