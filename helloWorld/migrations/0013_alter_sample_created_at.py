# Generated by Django 5.0.3 on 2024-05-02 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0012_alter_sample_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 2, 13, 44, 10, 679881)),
        ),
    ]
