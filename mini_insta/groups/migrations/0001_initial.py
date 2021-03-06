# Generated by Django 3.0.7 on 2020-06-17 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_group', models.CharField(max_length=256, unique=True)),
                ('description_of_group', models.TextField(blank=True, null=True)),
                ('members', models.ManyToManyField(related_name='members', related_query_name='member', to='accounts.User')),
                ('posts_in_group', models.ManyToManyField(to='posts.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
