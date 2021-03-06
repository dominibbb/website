# Generated by Django 3.0.7 on 2020-08-05 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20200720_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailChangeAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_key', models.CharField(max_length=42)),
                ('new_email', models.EmailField(max_length=125)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_change', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
