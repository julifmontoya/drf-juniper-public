# Generated by Django 5.0.6 on 2024-06-21 01:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0004_alter_hotel_city_alter_hotelcategory_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelDoLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('method', models.CharField(max_length=20)),
                ('request', models.TextField()),
                ('response', models.TextField()),
                ('error', models.BooleanField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
