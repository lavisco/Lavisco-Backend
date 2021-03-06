# Generated by Django 3.2.3 on 2021-06-07 14:53

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='meta_desc',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='meta_title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='customer.user.name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='meta_desc',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='meta_title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='cart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discountcode',
            name='meta_desc',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discountcode',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discountcode',
            name='meta_title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discountcode',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maincategory',
            name='meta_desc',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maincategory',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maincategory',
            name='meta_title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_desc',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariant',
            name='meta_desc',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariant',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariant',
            name='meta_title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariant',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='variant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='meta_desc',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='meta_title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
