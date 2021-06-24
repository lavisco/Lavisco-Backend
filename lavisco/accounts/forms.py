from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser
from product.models import Product


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'First Name', 'id': 'first-name-icon'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Last Name', 'id': 'first-name-icon'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Email', 'id': 'first-name-icon'
            })
        }


class SellerAddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['main_image', 'image2', 'image3', 'image4', 'image5', 'title', 'category', 'description',
                  'meta_title', 'meta_desc', 'meta_keywords']
        widgets = {
            'main_image': forms.FileInput(attrs={

            })
        }
