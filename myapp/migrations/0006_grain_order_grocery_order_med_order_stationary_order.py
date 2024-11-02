# Generated by Django 4.2.2 on 2024-10-17 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_dealer_details_delete_dealer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grain_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('qty', models.IntegerField()),
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
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Med_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('up', models.IntegerField()),
                ('qty', models.IntegerField()),
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
                ('qty', models.IntegerField()),
            ],
        ),
    ]
