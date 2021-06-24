from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.db import models as django_models
from django import forms
from . import models


class UserAdmin(DjangoUserAdmin):
    admin_priority = 1
    # Define admin model for custom User model with no email field.
    formfield_overrides = {
        django_models.ManyToManyField: {'widget': forms.SelectMultiple},
    }
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'get_full_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'shipping_address', 'billing_address', 'phone_number')


class StaticContentAdmin(admin.ModelAdmin):
    list_display = ('header', 'sub_header')


admin.site.register(models.CustomUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(models.CustomerProfile, CustomerAdmin)
admin.site.register(models.SellerProfile)
admin.site.register(models.Shipping)
admin.site.register(models.LaviscoStaticContent, StaticContentAdmin)

admin.site.site_header = 'Lavisco Admin Panel'
