# Generated by Django 4.2.9 on 2024-01-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_anniversary_account_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateField(auto_now_add=True, verbose_name='Date Joined'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateField(auto_now=True, verbose_name='Last Login'),
        ),
    ]
