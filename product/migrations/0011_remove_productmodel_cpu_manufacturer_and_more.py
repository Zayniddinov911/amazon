# Generated by Django 4.0.2 on 2022-04-14 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_brandmodel_productmodel_cpu_manufacturer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='CPU_manufacturer',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='Item_name',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='card_description',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='display',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='memory_storage',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='operating_system',
        ),
    ]
