# Generated by Django 5.0.3 on 2024-05-02 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 5, 2, 13, 38, 22, 293152)),
        ),
    ]
