from django import forms
from django.templatetags.static import static
from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].help_text = None

    class Meta:
        model = Product
        fields = ['seller', 'title', 'category', 'base_price', 'description', 'main_image', 'image2', 'image3', 'image4',
                  'image5', 'meta_title', 'meta_desc', 'meta_keywords']
        widgets = {
            'seller': forms.Select(attrs={'class': '', 'style': 'width: 200px;'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
            'base_price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'main_image': forms.FileInput({'class': 'dropify'}),
            'image2': forms.FileInput({
                'class': 'dropify'
            }),
            'image3': forms.FileInput({
                'class': 'dropify'
            }),
            'image4': forms.FileInput({
                'class': 'dropify'
            }),
            'image5': forms.FileInput({
                'class': 'dropify'
            }),
            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control'}),
        }
