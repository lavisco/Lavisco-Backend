from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('discount/code', views.DiscountCodeViewSet, basename='discount-code')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('cart', views.CartViewSet, basename='cart')
router.register('cart/item', views.CartItemViewSet, basename='cart-item')
router.register('variant', views.ProductVariantViewSet, basename='product-variant')
router.register('', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]
