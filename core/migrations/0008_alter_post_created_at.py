# Generated by Django 5.1.4 on 2024-12-27 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_followerscount_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 27, 21, 28, 45, 779340)),
        ),
    ]
