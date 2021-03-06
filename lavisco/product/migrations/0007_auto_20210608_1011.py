# Generated by Django 3.2.3 on 2021-06-08 10:11

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_cart_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('meta_title', models.CharField(max_length=50)),
                ('meta_desc', models.CharField(max_length=200)),
                ('meta_keywords', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='media/category')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='parent_category',
        ),
        migrations.DeleteModel(
            name='MainCategory',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='product.Category'),
        ),
    ]
