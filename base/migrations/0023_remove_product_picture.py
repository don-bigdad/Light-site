# Generated by Django 4.1 on 2022-11-01 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_remove_product_some_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='picture',
        ),
    ]
