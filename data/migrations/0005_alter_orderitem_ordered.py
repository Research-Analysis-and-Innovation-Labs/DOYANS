# Generated by Django 4.1.4 on 2023-01-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(),
        ),
    ]
