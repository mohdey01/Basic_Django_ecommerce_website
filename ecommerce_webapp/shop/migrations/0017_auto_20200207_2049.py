# Generated by Django 3.0 on 2020-02-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200207_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='orderupdate_orderid',
            field=models.IntegerField(default=0),
        ),
    ]
