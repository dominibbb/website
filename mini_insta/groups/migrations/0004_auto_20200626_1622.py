# Generated by Django 3.0.7 on 2020-06-26 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20200617_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='user',
            new_name='admin_of_group',
        ),
    ]