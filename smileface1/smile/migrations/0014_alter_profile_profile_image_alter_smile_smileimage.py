# Generated by Django 4.0.4 on 2022-06-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smile', '0013_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='', upload_to='smile/images/'),
        ),
        migrations.AlterField(
            model_name='smile',
            name='smileImage',
            field=models.ImageField(default='', upload_to='smile/images/'),
        ),
    ]