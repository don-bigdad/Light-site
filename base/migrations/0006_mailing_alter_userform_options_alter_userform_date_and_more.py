# Generated by Django 4.1 on 2022-08-31 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_userform_date_alter_userform_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mailing_start_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='userform',
            options={'ordering': ('time',)},
        ),
        migrations.AlterField(
            model_name='userform',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='userform',
            name='time',
            field=models.TimeField(),
        ),
    ]