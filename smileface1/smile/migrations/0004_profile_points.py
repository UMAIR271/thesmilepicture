# Generated by Django 4.0.4 on 2022-06-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0003_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]