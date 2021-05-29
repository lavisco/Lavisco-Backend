from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        return self.password

    def get_name(self):
        return str(self.email.split("@")[0])


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customers')
    avatar = models.ImageField(upload_to='media/customer', null=True, blank=True)
    shipping_address = models.CharField(max_length=150, null=True, blank=True)
    billing_address = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{0}'s Buyer profile".format(self.user)


class SellerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller')
    avatar = models.ImageField(upload_to='media/seller', null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.user.name:
            return str(self.user.name)
        else:
            return str(self.user.get_name())


class CustomerOrder(models.Model):
    statuses = (('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Failed', 'Failed'))
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='customer_orders')
    status = models.CharField(choices=statuses, max_length=20, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)
    item = models.IntegerField()
    order_price = models.IntegerField()

    def __str__(self):
        return self.customer.user.name