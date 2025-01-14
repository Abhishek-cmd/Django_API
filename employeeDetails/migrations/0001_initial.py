# Generated by Django 5.0.3 on 2024-04-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField(max_length=12)),
                ('address', models.TextField(max_length=500, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('joined_at', models.DateField()),
            ],
        ),
    ]
