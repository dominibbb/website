# Generated by Django 3.0.7 on 2020-06-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200619_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_of_publication',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]