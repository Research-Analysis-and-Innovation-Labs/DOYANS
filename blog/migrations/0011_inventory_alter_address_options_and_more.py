# Generated by Django 4.1 on 2022-08-25 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_author_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Author Address'},
        ),
        migrations.RemoveField(
            model_name='author',
            name='publisher',
        ),
        migrations.AddField(
            model_name='blog',
            name='publisher',
            field=models.ManyToManyField(to='blog.publisher'),
        ),
        migrations.AddField(
            model_name='blog',
            name='inventory',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.inventory'),
        ),
    ]
