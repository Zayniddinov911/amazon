# Generated by Django 4.0.2 on 2022-05-31 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customermodel',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'customers'},
        ),
    ]
