# Generated by Django 3.0.7 on 2020-06-19 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200619_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_of_publication',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 19, 13, 57, 27, 497888)),
        ),
    ]
