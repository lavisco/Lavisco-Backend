from rest_framework import viewsets
from django.shortcuts import render
from . import serializers
from . import models


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartSerializer
    queryset = models.Cart.objects.all()


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartItemSerializer
    queryset = models.CartItem.objects.all()


class ProductVariantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductVariantSerializer
    queryset = models.ProductVariant.objects.all()


class DiscountCodeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DiscountCodeSerializer
    queryset = models.DiscountCode.objects.all()
