# Generated by Django 3.2.3 on 2021-06-04 14:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0002_shipping'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaviscoAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('sub_header', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='LaviscoContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('sub_header', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='LaviscoCookiePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('sub_header', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='LaviscoFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('sub_header', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='LaviscoTermsConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('sub_header', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='save_for_future',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='LaviscoProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.laviscoaboutus')),
                ('contact_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.laviscocontactus')),
                ('cookie_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.laviscocookiepolicy')),
                ('terms_conditions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.laviscotermsconditions')),
            ],
        ),
    ]
