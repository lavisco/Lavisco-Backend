"""lavisco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from accounts.views import SellerOnBoardView, SellerDashboardView, SellerAccountView, SellerSignupView, SellerLoginView, \
    SellerOrderView, SellerProductsView, SellerMessagesView, SellerLogoutView, SellerAddProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('drf_registration.urls')),
    path('api/v1/users/', include('accounts.urls')),
    path('api/v1/products/', include('product.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('seller/onboard', SellerOnBoardView.as_view(), name='seller-onboard'),
    path('seller/dashboard', SellerDashboardView.as_view(), name='seller-dashboard'),
    path('seller/account', SellerAccountView.as_view(), name='seller-account'),
    path('seller/signup', SellerSignupView.as_view(), name='seller-signup'),
    path('seller/login', SellerLoginView.as_view(), name='seller-login'),
    path('seller/logout', SellerLogoutView.as_view(), name='seller-logout'),
    path('seller/orders', SellerOrderView.as_view(), name='seller-orders'),
    path('seller/products', SellerProductsView.as_view(), name='seller-products'),
    path('seller/add/product', SellerAddProductView.as_view(), name='seller-add-product'),
    path('seller/messages', SellerMessagesView.as_view(), name='seller-messages')

]
# admin.site.site_header = "Lavisco Admin Panel"
# admin.site.site_title = "Lavisco Admin Portal"
# admin.site.index_title = "Welcome to Lavisco Website Admin Panel"
