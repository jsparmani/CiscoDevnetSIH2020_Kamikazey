# Generated by Django 2.2.10 on 2020-08-01 16:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_auto_20200801_2218'),
    ]

    operations = [
        migrations.RemoveField(model_name='contractor', name='username',),
        migrations.AlterField(model_name='attendance', name='date', field=models.DateField(default=datetime.datetime(2020, 8, 1, 16, 53, 4, 619662, tzinfo=utc)),),
        migrations.AlterField(model_name='wastage', name='date', field=models.DateField(default=datetime.datetime(2020, 8, 1, 16, 53, 4, 617668, tzinfo=utc)),),
    ]