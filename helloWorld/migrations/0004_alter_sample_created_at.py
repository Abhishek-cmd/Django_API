# Generated by Django 5.0.3 on 2024-04-03 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0003_alter_sample_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 3, 13, 30, 40, 318733)),
        ),
    ]
