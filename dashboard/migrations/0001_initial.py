# Generated by Django 4.1 on 2022-08-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default=None, max_length=100)),
                ('name', models.CharField(blank=True, default=None, max_length=100)),
            ],
        ),
    ]
