# Generated by Django 4.1 on 2022-08-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_author_address_blog_author_alter_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
    ]
