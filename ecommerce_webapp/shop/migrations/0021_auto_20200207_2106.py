# Generated by Django 3.0 on 2020-02-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20200207_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='order_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='orderupdate_orderid',
            field=models.IntegerField(),
        ),
    ]
