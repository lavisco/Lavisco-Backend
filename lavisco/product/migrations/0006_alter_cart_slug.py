# Generated by Django 3.2.3 on 2021-06-07 14:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210607_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='customer'),
        ),
    ]