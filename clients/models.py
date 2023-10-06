from datetime import date

from django.db import models


class Client(models.Model):
    """Class for Client instances"""
    
    name = models.CharField(max_length=200, verbose_name="Name")
    surname = models.CharField(max_length=200, verbose_name="Surname")
    street_address = models.CharField(max_length=200, verbose_name="Address")
    city = models.CharField(max_length=100, verbose_name="City")
    postal_code = models.CharField(max_length=6, verbose_name="Postcode")
    email = models.EmailField(max_length=200, verbose_name="Email")
    phone_number = models.CharField(max_length=16, verbose_name="Phone number")

    def __str__(self):
        return f"{self.name} {self.surname}"

 
class Insurance(models.Model):

    TYPES_OF_INSURANCE = [
        ("Property", "Property insurance"),
        ("Emergency", "Contingency insurance"),
        ("Life", "Life insurance"),
        ("Accident", "Accident insurance"),
        ("Liability", "Liability insurance")
    ]

    insurance_type = models.CharField(max_length=30, choices=TYPES_OF_INSURANCE, verbose_name="Insurance type")
    subject = models.CharField(max_length=100, verbose_name="Subject of insurance")
    amount = models.PositiveIntegerField(verbose_name="Sum insured")
    date_from = models.DateField(default=date.today, verbose_name="Insured from")
    date_to = models.DateField(default=date.today, verbose_name="Insured to")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.insurance_type}: {self.subject}, {self.amount}"


class Payment(models.Model):
    """Class for Payment system"""

    name = models.CharField(max_length=200, verbose_name="Name")
    surname = models.CharField(max_length=200, verbose_name="Surnmae")
    email = models.EmailField(max_length=200, verbose_name="Email")
    date_to_c = models.DateField(default=date.today, verbose_name="Validity")
    card_number = models.CharField(max_length=20, verbose_name="Card number")
    cvv = models.CharField(max_length=3, verbose_name="CVV")

    def _str_(self):
        return f"{self.name} {self.surname}"
