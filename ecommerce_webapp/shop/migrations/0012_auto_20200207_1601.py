# Generated by Django 3.0 on 2020-02-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200207_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='orderupdate_orderid',
            field=models.IntegerField(),
        ),
    ]
