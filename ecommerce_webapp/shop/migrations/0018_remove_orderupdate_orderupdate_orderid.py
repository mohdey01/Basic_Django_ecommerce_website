# Generated by Django 3.0 on 2020-02-07 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200207_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderupdate',
            name='orderupdate_orderid',
        ),
    ]
