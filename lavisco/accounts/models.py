from autoslug import AutoSlugField
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='email')
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = ' Users'

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_name(self):
        return str(self.email.split("@")[0])


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customers')
    avatar = models.ImageField(upload_to='media/customer', null=True, blank=True)
    shipping_address = models.CharField(max_length=150, null=True, blank=True)
    billing_address = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='user')

    class Meta:
        db_table = 'Customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return "{0}'s Buyer profile".format(self.user)

    def get_user(self):
        return self.user


class SellerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller')
    avatar = models.ImageField(upload_to='media/seller', null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='user')

    class Meta:
        db_table = 'Seller'
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        if self.user.get_full_name():
            return str(self.user.get_full_name())
        else:
            return str(self.user.get_name())


class CustomerOrder(models.Model):
    statuses = (('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Failed', 'Failed'))
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='customer_orders')
    status = models.CharField(choices=statuses, max_length=20, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)
    item = models.IntegerField()
    order_price = models.IntegerField()
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='status')

    class Meta:
        db_table = 'Customer Order'
        verbose_name = 'Customer Order'
        verbose_name_plural = 'Customer Orders'

    def __str__(self):
        return self.customer.user.get_full_name()


class Shipping(models.Model):
    first_method = 'Express-2 Day'
    second_method = 'Express-4 Day'
    third_method = 'Express-7 Day'
    shipping_method = (
        (first_method, 'Express-2 Day'), (second_method, 'Express-4 Day'), (third_method, 'Express-7 Day'))

    customer = models.OneToOneField(CustomerProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=False)
    company = models.CharField(max_length=100, null=True, blank=True)
    address_one = models.CharField(max_length=100, null=True, blank=False)
    address_two = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=False)
    state_or_province = models.CharField(max_length=50, null=True, blank=False)
    postal_code = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=50, null=True, blank=False)
    shipping_method = models.CharField(max_length=20, choices=shipping_method, null=True, blank=False)
    save_for_future = models.BooleanField(default=False, null=True, blank=True)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='first_name')

    class Meta:
        db_table = 'Shipping'
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shipping'

    def __str__(self):
        return self.shipping_method


class LaviscoStaticContent(models.Model):
    page_key = models.CharField(max_length=200)
    header = models.CharField(max_length=200)
    sub_header = models.CharField(max_length=200)
    content = RichTextField()
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='header')

    class Meta:
        db_table = 'Static Content'
        verbose_name = 'Static Content'
        verbose_name_plural = 'Static Content'

    def __str__(self):
        return self.header
