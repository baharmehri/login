# Generated by Django 4.2.14 on 2024-08-09 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_bannedip_banned_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannedip',
            name='banned_until',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 11, 46, 18, 152107, tzinfo=datetime.timezone.utc)),
        ),
    ]
