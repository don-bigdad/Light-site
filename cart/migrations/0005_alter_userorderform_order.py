# Generated by Django 4.1 on 2022-09-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_userorderform_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorderform',
            name='order',
            field=models.TextField(max_length=400),
        ),
    ]
