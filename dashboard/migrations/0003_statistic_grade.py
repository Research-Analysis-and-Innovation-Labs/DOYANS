# Generated by Django 4.1 on 2022-08-25 08:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_statistic_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='grade',
            field=models.IntegerField(blank=True, default=0, max_length=10, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]