# Generated by Django 3.0.7 on 2020-06-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200624_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts_image'),
        ),
    ]
