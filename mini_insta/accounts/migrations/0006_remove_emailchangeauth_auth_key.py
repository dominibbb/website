# Generated by Django 3.0.7 on 2020-08-05 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_emailchangeauth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailchangeauth',
            name='auth_key',
        ),
    ]
