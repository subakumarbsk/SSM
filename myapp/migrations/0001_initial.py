# Generated by Django 4.2.2 on 2024-10-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=30)),
                ('med_combination', models.CharField(max_length=100)),
                ('med_dealer', models.CharField(max_length=50)),
                ('med_category', models.CharField(max_length=20)),
                ('med_mrp', models.IntegerField()),
                ('med_up', models.IntegerField()),
                ('med_qty', models.IntegerField()),
                ('med_unit', models.CharField(max_length=6)),
            ],
        ),
    ]
