# Generated by Django 2.2.10 on 2020-08-01 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_detection', '0026_auto_20200801_2358'),
    ]

    operations = [
        migrations.AlterField(model_name='filehash', name='datetime', field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 0, 33, 50, 836209)),),
    ]