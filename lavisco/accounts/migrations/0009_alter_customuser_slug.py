# Generated by Django 3.2.3 on 2021-06-08 08:10

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210608_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='email'),
        ),
    ]
