# Generated by Django 4.0.2 on 2022-04-14 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productmodel_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='brand',
        ),
        migrations.DeleteModel(
            name='BrandModel',
        ),
    ]