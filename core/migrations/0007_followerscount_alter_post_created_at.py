# Generated by Django 5.1.4 on 2024-12-26 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 26, 10, 29, 38, 752931)),
        ),
    ]
