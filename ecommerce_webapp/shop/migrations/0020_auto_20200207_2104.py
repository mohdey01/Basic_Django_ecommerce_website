# Generated by Django 3.0 on 2020-02-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_orderupdate_orderupdate_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
