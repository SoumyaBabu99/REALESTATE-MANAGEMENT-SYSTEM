from django import forms
from .models import *



class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = adminuser
        fields = '__all__'

class AdminLoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=15,widget=forms.PasswordInput)

# class AdminRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = adminuser
#         fields = ['username', 'email', 'password']
        # Other fields from the AdminRegistration model as needed

# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     # Other form fields if needed


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location','features']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['property', 'rent_cost', 'type']
        # Add more fields as needed

class TenantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proofs', 'password', 'phone']
        widgets = {
            'password': forms.PasswordInput(),
        }


class Tenant_Login(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=15,widget=forms.PasswordInput)

class RentalInformationForm(forms.ModelForm):
    class Meta:
        model = RentalInformation
        fields = ['tenant', 'unit', 'agreement_end_date', 'monthly_rent_date']
        # Add more fields as needed