# Generated by Django 2.2.6 on 2019-12-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='soonMovie',
            fields=[
                ('movieid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=4)),
                ('length', models.CharField(max_length=10)),
                ('genres', models.CharField(max_length=100)),
                ('poster', models.URLField(default='')),
                ('plot', models.CharField(max_length=500)),
                ('trailer', models.URLField(default='')),
            ],
        ),
    ]
