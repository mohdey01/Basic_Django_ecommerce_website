# Generated by Django 3.0 on 2020-02-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20200207_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]