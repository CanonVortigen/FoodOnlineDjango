# Generated by Django 5.0.1 on 2024-01-24 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='fooditem',
            options={'verbose_name': 'Food Item', 'verbose_name_plural': 'Food Items'},
        ),
    ]
