# Generated by Django 5.0 on 2024-02-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=14, verbose_name='تلفن همراه'),
        ),
    ]