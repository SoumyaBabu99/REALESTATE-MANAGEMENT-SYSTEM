from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import re
from django.core.exceptions import ValidationError


def contact_validate(value):
    rule = r"^[9876][0-9]{9}$"
    match = re.fullmatch(rule, value)
    if not match:
        raise ValidationError("Please enter a valid contact number")

def email_validate(value):
    rule = r"^[a-z]+[0-9][_]?[a-z0-9]*@gmail.com"
    match = re.fullmatch(rule, value)
    if not match:
        raise ValidationError("Please enter a valid email")

class adminuser(models.Model):
    username=models.CharField(max_length=30,unique=True)
    email=models.EmailField(unique=True,validators=[email_validate])
    contact=models.CharField(max_length=10,validators=[contact_validate])
    password=models.CharField(max_length=15)

    def _str_(self):
        return self.username


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=100)
    features=models.TextField()
    # Other property details like features

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    UNIT_TYPES = (
        ('1BHK', '1 Bedroom Hall Kitchen'),
        ('2BHK', '2 Bedroom Hall Kitchen'),
        ('3BHK', '3 Bedroom Hall Kitchen'),
        ('4BHK', '4 Bedroom Hall Kitchen'),
    )
    type = models.CharField(max_length=4, choices=UNIT_TYPES)

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    document_proofs = models.FileField(upload_to='tenant_documents/') 
    password=models.CharField(max_length=100)
    phone=models.IntegerField()
     # Example field for document proofs

   
    # Other tenant details like document proofs

class RentalInformation(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()  # Day of the month for rent payment
