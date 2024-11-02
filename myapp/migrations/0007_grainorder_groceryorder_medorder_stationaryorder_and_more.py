# Generated by Django 4.2.2 on 2024-10-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_grain_order_grocery_order_med_order_stationary_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrainOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MedOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StationaryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Grain_Order',
        ),
        migrations.DeleteModel(
            name='Grocery_Order',
        ),
        migrations.DeleteModel(
            name='Med_Order',
        ),
        migrations.DeleteModel(
            name='Stationary_Order',
        ),
    ]
