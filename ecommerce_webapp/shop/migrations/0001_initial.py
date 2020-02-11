# Generated by Django 3.0 on 2019-12-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_description', models.CharField(max_length=300)),
                ('product_publishDate', models.DateField()),
            ],
        ),
    ]
