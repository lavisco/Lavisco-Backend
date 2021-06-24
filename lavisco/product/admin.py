from django.contrib import admin
from django.db import models as django_models
from django import forms

from . import models
from .forms import ProductForm


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['category__name']
    list_display = ['title', 'get_category', 'base_price']
    form = ProductForm
    # formfield_overrides = {
    #     django_models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 200px'})},
    #     django_models.ManyToManyField: {'widget': forms.SelectMultiple(attrs={'style': 'width: 200px'})},
    #     django_models.PositiveIntegerField: {'widget': forms.NumberInput(attrs={'style': 'width: 150px'})},
    #     django_models.ImageField: {'widget': forms.FileInput(attrs={'style': 'width: 200px'})},
    # }
    fieldsets = (
        (None, {'fields': (
            ('seller', 'title'),
            ('category', 'base_price'),
            'description',
            ('main_image', 'image2'),
            ('image3', 'image4'),
            ('image5', 'meta_title'),
            ('meta_desc', 'meta_keywords'))}),
    )


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'parent_category']
    list_display = ['name', 'parent_category']
    # fieldsets = (
    #
    # )


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
# Register your models here.
