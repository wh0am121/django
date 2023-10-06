from django import forms

from . models import Client, Insurance, Payment


class CreateClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ["name", "surname", "street_address", "city", "postal_code", "email", "phone_number"]


class CreateInsuranceForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = ["insurance_type", "subject", "amount", "date_from", "date_to"]


class CreatePaymentForm(forms.ModelForm):
    """Curstom form for Client instance creation."""

    class Meta:
        model = Payment
        fields = ["card_number", "name", "surname", "date_to_c", "cvv", "email"]
