# Generated by Django 2.2.6 on 2019-11-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191124_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
    ]