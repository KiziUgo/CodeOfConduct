# Generated by Django 3.0.4 on 2020-10-11 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0003_postccb_year_first_decl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postccb',
            old_name='year_First_Decl',
            new_name='actual_year_of_First_Decl',
        ),
    ]
