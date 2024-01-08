from django.urls import path
from . import views
from .views import *

urlpatterns = [
  
    path('register/', Adminregister.as_view(), name='register'),
    path('login/', login_admin.as_view(), name='login'),
    path('create/', views.create_property, name='create_property'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('property_pro/<int:property_id>/', views.property_profile_view, name='property_profile'),
    path('add-unit/', views.add_unit, name='add-unit'),
    path('edit-unit/<int:unit_id>/', views.edit_unit, name='edit_unit'),
    path('delete-unit/<int:unit_id>/', views.delete_unit, name='delete_unit'),
    path('property/<int:property_id>/tenant/', views.property_with_tenant_view, name='property_with_tenant'),
    # path('tenant_create/', views.create_tenant, name='create_tenant'),
    # path('list/', views.tenant_list, name='tenant_list'),
    # path('detail/<int:tenant_id>/', views.tenant_detail, name='tenant_detail'),
    path('register-tenant/', views.register, name='register-tenant'),
    # Login URL
    path('login-tenant/', views.TenentLoginView.as_view(), name='login-tenant'),
    
    path('tenant/<int:tenant_id>/', views.tenant_profile_view, name='tenant_profile'),
    path('tenant/<int:tenant_id>/rental/', views.tenant_rental_info_view, name='tenant_rental_info')
    # Other URL patterns
]
