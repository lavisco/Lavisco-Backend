from rest_framework import serializers
from . import models


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['name', 'email', 'password1', 'password2']
        read_only_fields = ('email',)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SellerProfile
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerProfile
        fields = '__all__'


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipping
        fields = '__all__'


class StaticContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LaviscoStaticContent
        fields = ['header', 'sub_header', 'content']

