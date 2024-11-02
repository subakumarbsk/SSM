# Generated by Django 4.2.2 on 2024-10-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_ec_bill_medical_medicine_bill_product_product_bill_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer', models.CharField(max_length=40)),
                ('gst_no', models.CharField(max_length=20)),
                ('dd', models.DateField()),
                ('d_category', models.CharField(max_length=30)),
                ('d_address', models.CharField(max_length=300)),
                ('d_mobile_no', models.IntegerField()),
                ('contact_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Dealer',
        ),
    ]
