from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["id", "name", "email", "phone", "address", "city", "state", "zipcode",]