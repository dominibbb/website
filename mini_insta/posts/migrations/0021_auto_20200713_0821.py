# Generated by Django 3.0.7 on 2020-07-13 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0020_auto_20200713_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_author', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
