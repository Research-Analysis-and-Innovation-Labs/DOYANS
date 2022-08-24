# Generated by Django 4.1 on 2022-08-24 07:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=None)),
                ('body', models.TextField(null=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(5)])),
                ('is_bestselling', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]