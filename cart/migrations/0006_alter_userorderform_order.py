# Generated by Django 4.1 on 2022-09-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_userorderform_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorderform',
            name='order',
            field=models.TextField(auto_created=True, max_length=400),
        ),
    ]