# Generated by Django 4.1.7 on 2023-10-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_remove_salescreditnote1_scredit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='salescreditnote',
            fields=[
                ('screditid', models.AutoField(primary_key=True, serialize=False, verbose_name='pdid')),
                ('credit_no', models.IntegerField(default=1000)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('creditdate', models.DateField(null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('supply', models.CharField(max_length=150, null=True)),
                ('billno', models.CharField(max_length=100, null=True)),
                ('subtotal', models.CharField(max_length=100, null=True)),
                ('shipping_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('taxamount', models.CharField(max_length=100, null=True)),
                ('grandtotal', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='salescreditnote1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100, null=True)),
                ('hsn', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('discount', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('scredit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.salescreditnote')),
            ],
        ),
    ]