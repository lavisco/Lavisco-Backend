from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework import viewsets
from . import serializers
from . import models

# Create your views here.
from .forms import SignUpForm, SellerAddProductForm


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserListSerializer
    queryset = models.CustomUser.objects.all()


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SellerSerializer
    queryset = models.SellerProfile.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.CustomerProfile.objects.all()


class ShippingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShippingSerializer
    queryset = models.Shipping.objects.all()


class StaticContentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StaticContentSerializer
    queryset = models.LaviscoStaticContent.objects.all()


class SellerOnBoardView(View):

    def get(self, request):
        return render(request, 'accounts/seller-onboard.html', {})

    def post(self, request):
        pass


class SellerDashboardView(View):

    def get(self, request):
        return render(request, 'accounts/seller-dashboard.html', {})

    def post(self, request):
        pass


class SellerAccountView(View):

    def get(self, request):
        form = SignUpForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/seller-account.html', context)

    def post(self, request):
        pass


class SellerSignupView(View):

    def get(self, request):
        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/seller-signup.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return HttpResponse(
                'We have received your request. You will be informed about the process via email. Thank you')
        else:
            form = SignUpForm(request.POST)
            context = {
                'form': form
            }
            return render(request, 'accounts/seller-signup.html', context)


class SellerLoginView(View):

    def get(self, request):
        return render(request, 'accounts/seller-login.html', {})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print('user ', user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('seller-account')
            else:
                messages.error(request, 'The account is not active')
                return redirect('seller-login')
        else:
            messages.error(request, 'Wrong Email or Password')
            return redirect('seller-login')


class SellerOrderView(View):

    def get(self, request):
        return render(request, 'accounts/seller-orders.html', {})


class SellerProductsView(View):

    def get(self, request):
        return render(request, 'accounts/seller-products.html', {})


class SellerAddProductView(View):
    def get(self, request):
        form = SellerAddProductForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/seller-add-product.html', context)

    def post(self, request):
        pass


class SellerMessagesView(View):

    def get(self, request):
        return render(request, 'accounts/seller-messages.html', {})


class SellerLogoutView(View):

    def get(self, request):
        logout(request)
        return render(request, 'accounts/seller-login.html', {})
