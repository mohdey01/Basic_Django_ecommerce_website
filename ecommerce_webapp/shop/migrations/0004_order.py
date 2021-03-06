# Generated by Django 3.0 on 2020-01-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('orderitems_json', models.CharField(max_length=4000)),
                ('order_name', models.CharField(max_length=50)),
                ('order_email', models.CharField(default='', max_length=50)),
                ('order_phone', models.CharField(default='', max_length=50)),
                ('order_address', models.CharField(default='', max_length=50)),
                ('order_city', models.CharField(default='', max_length=50)),
                ('order_state', models.CharField(default='', max_length=50)),
                ('order_zip', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
