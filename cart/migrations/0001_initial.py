# Generated by Django 4.1 on 2022-09-03 19:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrderForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Input number in format xxx xxx xxxx', regex='^(\\d{3}[- .]?){2}\\d{4}$')])),
                ('is_processed', models.BooleanField(default=False)),
            ],
        ),
    ]