# Generated by Django 3.2 on 2025-01-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
