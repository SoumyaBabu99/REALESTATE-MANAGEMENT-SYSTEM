from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import LoginForm  # Import the login form if you create a custom form
from .forms import *  # Import the registration form
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django .views import generic
from .models import *
from django.views import View
from .forms import *


# def register_admin(request):
#    form_class = AdminRegistrationForm
#    template_name = 'adminregister.html'
#    success_url = reverse_lazy('admin_login')


# Admin Register Views
class Adminregister(generic.CreateView):
    form_class = AdminRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

# Admin Login Views
class login_admin(View):
    form_class = AdminLoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = adminuser.objects.filter(email=email, password=password).first()

            if user:
                request.session['u_id'] = user.id
                return redirect('create_property') # Replace 'propertyview' with your actual URL name
            else:
                return HttpResponse('Login failed: Incorrect username or password.')
        else:
            # Display form errors in the response
            return HttpResponse(f'Form data is invalid. Errors: {form.errors}')
# Property create Views
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save()
            return redirect('http://127.0.0.1:8000/realestate_app/add-unit/', property_id=property.id)  # Redirect to property detail view
    else:
        form = PropertyForm()
    
    return render(request, 'create_property.html', {'form': form})
# Add Units to Each Properties
def add_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit_type = form.cleaned_data['type']
            
            # Check if a unit with the same type exists for the property
            existing_unit = Unit.objects.filter(property=form.cleaned_data['property'], type=unit_type).first()
            
            if existing_unit:
                # If a unit with the same type exists, redirect to the property detail page
                return redirect(f'/realestate_app/property_pro/{existing_unit.property.id}/')

            # If no existing unit with the same type, save the form and redirect
            unit = form.save()
            property_id = unit.property.id
            return redirect(f'/realestate_app/property_pro/{property_id}/')

    else:
        form = UnitForm()
    return render(request, 'add_unit.html', {'form': form})
def edit_unit(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_list')  # Redirect to a view showing the list of units
    else:
        form = UnitForm(instance=unit)
    return render(request, 'edit_unit.html', {'form': form})

def delete_unit(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    if request.method == 'POST':
        unit.delete()
        return redirect('unit_list')  # Redirect to a view showing the list of units
    return render(request, 'delete_unit.html', {'unit': unit})


# This Property_detail and Property_profile_view is used to View property profile
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    # Other necessary actions to prepare property details if needed
    return render(request, 'property_detail.html', {'property': property})

def property_profile_view(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    units = property.unit_set.all()  # Retrieve all units for the property
    context = {
        'property': property,
        'units': units
    }
    return render(request, 'property_profile.html', context)

# You can create a view to show property profile with tenant information for each unit
def register(request):
    if request.method == 'POST':
        form = TenantRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Hash the password before saving
            tenant = form.save(commit=False)
            tenant.password = make_password(form.cleaned_data['password'])
            tenant.save()
            return redirect('login-tenant')
    else:
        form = TenantRegistrationForm()
    return render(request, 'registration_tenant.html', {'form': form})

"""def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        try:
            tenant = Tenant.objects.get(name=username)
            if tenant.check_password(password):
                # Perform login action
                return redirect('dashboard')  # Redirect to the dashboard or any other page
            else:
                error = "Invalid username or password."
                return render(request, 'tenant_login.html', {'error': error})
        except Tenant.DoesNotExist:
            error = "Invalid username or password."
            return render(request, 'tenant_login.html', {'error': error})
    return render(request, 'tenant_login.html')"""

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .models import Tenant

def login_tenant(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user exists and the password is correct
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            # Redirect to the dashboard or any other page after successful login
            return redirect('dashboard')
        else:
            error = "Invalid username or password."
            return render(request, 'login_tenant.html', {'error': error})
    
    return render(request, 'login_tenant.html')



def property_with_tenant_view(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    units = property.unit_set.all()  # Retrieve all units for the property
    context = {
        'property': property,
        'units': units
        # Include additional context for tenant information if needed
    }
    return render(request, 'property_with_tenant.html', context)
from django.contrib.auth.hashers import check_password

class TenentLoginView(generic.View):
    form_class = Tenant_Login
    template_name = 'tenant_login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            tenant = Tenant.objects.filter(name=name).first()

            if tenant and check_password(password, tenant.password):
                request.session['u_id'] = tenant.id
                return HttpResponse('login success')# Adjust this to your actual URL name
            else:
                return HttpResponse('Login failed: Incorrect username or password.')

        return HttpResponse('Invalid form data')

def tenant_profile_view(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    context = {
        'tenant': tenant
    }
    return render(request, 'tenant_profile.html', context)

def tenant_rental_info_view(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    rental_info = RentalInformation.objects.filter(tenant=tenant)
    context = {
        'tenant': tenant,
        'rental_info': rental_info
    }
    return render(request, 'tenant_rental_info.html', context)
