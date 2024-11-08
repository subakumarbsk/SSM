# Generated by Django 4.2.2 on 2024-10-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_medicine_delete_medical_alter_medicine_bill_med_amt1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=30)),
                ('pro_dealer', models.CharField(max_length=100)),
                ('pro_type', models.CharField(max_length=30)),
                ('pro_cat', models.CharField(max_length=30)),
                ('pro_mrp', models.IntegerField()),
                ('pro_up', models.IntegerField()),
                ('pro_gst', models.IntegerField()),
                ('pro_gst_price', models.FloatField()),
                ('pro_qty', models.IntegerField()),
                ('pro_unit', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Grain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veg_name', models.CharField(max_length=30)),
                ('veg_dealer', models.CharField(max_length=100)),
                ('veg_mar', models.IntegerField()),
                ('veg_category', models.CharField(max_length=20)),
                ('veg_mrp', models.IntegerField()),
                ('veg_up', models.IntegerField()),
                ('veg_mar_Price', models.IntegerField()),
                ('veg_gst', models.IntegerField()),
                ('with_gst', models.IntegerField()),
                ('veg_qty', models.IntegerField()),
                ('veg_unit', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Grain_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('gst_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grocery_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('gst_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('gst_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stationary_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('gst_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='GrainOrder',
        ),
        migrations.DeleteModel(
            name='GroceryOrder',
        ),
        migrations.DeleteModel(
            name='MedOrder',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='StationaryOrder',
        ),
        migrations.DeleteModel(
            name='veg_dhal',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='med_gst',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='med_mrp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='med_up',
            field=models.FloatField(),
        ),
    ]
