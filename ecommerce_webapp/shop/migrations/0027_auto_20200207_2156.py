# Generated by Django 3.0 on 2020-02-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20200207_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderupdate',
            name='orderupdate_orderid',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
