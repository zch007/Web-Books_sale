# Generated by Django 2.0.6 on 2020-09-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField()),
                ('origin_address', models.CharField(max_length=100)),
                ('total_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('carriage', models.IntegerField()),
            ],
            options={
                'db_table': 't_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 't_order_item',
                'managed': False,
            },
        ),
    ]
