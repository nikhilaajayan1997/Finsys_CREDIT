# Generated by Django 4.1.7 on 2023-10-29 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_challan_customer_e_waybills_e_waybill_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salescreditnote1',
            name='scredit',
        ),
        migrations.DeleteModel(
            name='salescreditnote',
        ),
        migrations.DeleteModel(
            name='salescreditnote1',
        ),
    ]
