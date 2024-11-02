# Generated by Django 4.2.2 on 2024-10-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_medicines_delete_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='EC_Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sim_name', models.CharField(max_length=50)),
                ('ec_paid', models.IntegerField()),
                ('ec_b1_d', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=30)),
                ('med_combination', models.CharField(max_length=100)),
                ('med_dealer', models.CharField(max_length=50)),
                ('med_category', models.CharField(max_length=20)),
                ('med_mrp', models.IntegerField()),
                ('med_up', models.IntegerField()),
                ('med_gst', models.IntegerField()),
                ('med_qty', models.IntegerField()),
                ('med_unit', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_dealer', models.CharField(max_length=50)),
                ('med_invoice', models.CharField(max_length=50)),
                ('med_invoice_d', models.DateField()),
                ('med_amt', models.IntegerField()),
                ('med_payment', models.CharField(max_length=20)),
                ('med_amt1', models.IntegerField()),
                ('med_bill_no', models.CharField(max_length=10)),
                ('med_b1_d', models.DateField()),
                ('med_amt2', models.IntegerField()),
                ('med_bill_no2', models.CharField(max_length=10)),
                ('med_b2_d', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=30)),
                ('pro_dealer', models.CharField(max_length=100)),
                ('pro_type', models.CharField(max_length=30)),
                ('pro_cat', models.CharField(max_length=30)),
                ('pro_mrp', models.IntegerField()),
                ('pro_up', models.IntegerField()),
                ('pro_gst', models.IntegerField()),
                ('pro_qty', models.IntegerField()),
                ('pro_unit', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_dealer', models.CharField(max_length=50)),
                ('pro_invoice', models.CharField(max_length=50)),
                ('pro_invoice_d', models.DateField()),
                ('pro_amt', models.IntegerField()),
                ('pro_payment', models.CharField(max_length=20)),
                ('pro_amt1', models.IntegerField()),
                ('pro_bill_no', models.CharField(max_length=10)),
                ('pro_b1_d', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='veg_dhal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veg_name', models.CharField(max_length=30)),
                ('veg_dealer', models.CharField(max_length=100)),
                ('veg_mar', models.IntegerField()),
                ('veg_category', models.CharField(max_length=20)),
                ('veg_mrp', models.IntegerField()),
                ('veg_up', models.IntegerField()),
                ('veg_gst', models.IntegerField()),
                ('veg_qty', models.IntegerField()),
                ('veg_unit', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='veg_dhal_bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veg_dealer', models.CharField(max_length=50)),
                ('veg_invoice', models.CharField(max_length=50)),
                ('veg_invoice_d', models.DateField()),
                ('veg_amt', models.IntegerField()),
                ('veg_payment', models.CharField(max_length=20)),
                ('veg_amt1', models.IntegerField()),
                ('veg_bill_no', models.CharField(max_length=10)),
                ('veg_b1_d', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Medicines',
        ),
    ]