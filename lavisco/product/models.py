from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, blank=True, default=None)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='media/category', default=None, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# class SubCategory(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=500, null=True, blank=True, default=None)
#     parent_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='subcategory')
#     meta_title = models.CharField(max_length=50)
#     meta_desc = models.CharField(max_length=200)
#     meta_keywords = models.CharField(max_length=50)
#     slug = AutoSlugField(populate_from='name')

    # def __str__(self):
    #     return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    category = models.ManyToManyField(Category, related_name='product')
    seller = models.ForeignKey('accounts.SellerProfile', on_delete=models.CASCADE, related_name='products',
                               default=None,
                               blank=False)
    base_price = models.PositiveIntegerField(null=True, blank=False, default=None)
    description = models.TextField()
    main_image = models.ImageField(upload_to='media/products', default=None, blank=False)
    image2 = models.ImageField(upload_to='media/products', blank=True)
    image3 = models.ImageField(upload_to='media/products', blank=True)
    image4 = models.ImageField(upload_to='media/products', blank=True)
    image5 = models.ImageField(upload_to='media/products', blank=True)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_category(self):
        return " | ".join([category.name for category in self.category.all()])

    def __str__(self):
        if self.seller.user.get_full_name():
            return '{} by {}'.format(self.title, self.seller.user.get_full_name())
        else:
            return '{} by {}'.format(self.title, self.seller.user.get_name())


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants', default=None)
    variant = models.CharField(max_length=100, default='', null=True, blank=False)
    variant_value = models.CharField(max_length=100, default=None, null=True, blank=False)
    price = models.PositiveIntegerField(null=True, blank=False)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='variant')

    class Meta:
        verbose_name = 'Product Variant'
        verbose_name_plural = 'Product Variant'

    def __str__(self):
        return '{} -- Rs. {}'.format(self.variant_value, self.price)


class ProductRating(models.Model):
    customer = models.ForeignKey('accounts.CustomerProfile', on_delete=models.CASCADE, related_name='customer_ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    ratings = models.PositiveIntegerField(default=0, null=True, blank=False)
    review = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Product Rating'
        verbose_name_plural = 'Product Ratings'


class Cart(models.Model):
    customer = models.ForeignKey('accounts.CustomerProfile', on_delete=models.CASCADE, related_name='cart',
                                 default=None)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)
    total_amount = models.PositiveIntegerField(null=True, blank=True, default=0)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='customer')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        if self.customer.user.get_full_name():
            return '{} has {} products of Rs {}'.format(self.customer.user.get_full_name(), self.total_products, self.total_amount)
        else:
            return '{} has {} products of Rs {}'.format(self.customer.user.get_name(), self.total_products,
                                                        self.total_amount)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    variant = models.ManyToManyField(ProductVariant, related_name='cart_items', default=None)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    sub_total = models.PositiveIntegerField(null=True, blank=True, default=0)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='cart')

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def get_subtotal(self):
        total = 0
        for variant in self.variant.all():
            total += variant.price
        return total

    def get_quantity(self):
        return self.variant.count()

    def get_product_id(self):
        return self.variant.first().product.id

    def __str__(self):
        return '{} has {} items of total Rs {} in cart'.format(self.cart.customer.user.name, self.get_quantity(),
                                                               self.get_subtotal())


class ProductGiftMessage(models.Model):
    customer = models.ForeignKey('accounts.CustomerProfile', on_delete=models.CASCADE, default=None, null=True,
                                 blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)


class ProductEngravingMessage(models.Model):
    customer = models.ForeignKey('accounts.CustomerProfile', on_delete=models.CASCADE, default=None, null=True,
                                 blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)


class DiscountCode(models.Model):
    code = models.CharField(max_length=30, unique=True)
    discount = models.FloatField(max_length=15)
    is_valid = models.BooleanField(default=True, null=True, blank=True)
    meta_title = models.CharField(max_length=50)
    meta_desc = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='code')

    class Meta:
        verbose_name = 'Discount Codes'
        verbose_name_plural = 'Discount Codes'

    def __str__(self):
        return self.code


class OrderItem(models.Model):
    order = models.ForeignKey('accounts.CustomerOrder', on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    total_price = models.IntegerField()

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
