# Generated by Django 3.0 on 2020-02-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200207_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
