# Generated by Django 3.2 on 2022-07-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCBForm', '0003_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
