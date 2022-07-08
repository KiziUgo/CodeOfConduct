# Generated by Django 3.0.4 on 2020-10-10 14:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterCCB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declarant_ID', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('rank', models.CharField(max_length=100, null=True)),
                ('date_issued', models.CharField(max_length=100, null=True)),
                ('date_sworn_to', models.CharField(max_length=100, null=True)),
                ('date_recieved', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterEFCC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declarant_ID', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('rank', models.CharField(max_length=100, null=True)),
                ('date_issued', models.CharField(max_length=100, null=True)),
                ('date_sworn_to', models.CharField(max_length=100, null=True)),
                ('date_recieved', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterICPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declarant_ID', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('rank', models.CharField(max_length=100, null=True)),
                ('date_issued', models.CharField(max_length=100, null=True)),
                ('date_sworn_to', models.CharField(max_length=100, null=True)),
                ('date_recieved', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostWelcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declarant_id', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostICPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.CharField(max_length=100, null=True)),
                ('declarant_id', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('other_names', models.CharField(max_length=100, null=True)),
                ('date_ob', models.CharField(max_length=100, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('cadre', models.CharField(max_length=100, null=True)),
                ('rank_at_FAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_FAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_confirmation', models.CharField(max_length=100, null=True)),
                ('rank_at_LAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_LAPPT', models.CharField(max_length=100, null=True)),
                ('rank_at_PAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_PAPPT', models.CharField(max_length=100, null=True)),
                ('Num_Of_YIS', models.CharField(max_length=100, null=True)),
                ('Num_Of_YPIS', models.CharField(max_length=100, null=True)),
                ('date_OR', models.CharField(max_length=100, null=True)),
                ('date_of_1st_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_2nd_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_3rd_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_4th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_5th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_6th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_7th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_8th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_9th_declaration', models.CharField(max_length=100, null=True)),
                ('action_taken', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('investigation_activities', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('envelop_number', models.CharField(max_length=100, null=True)),
                ('box_number', models.CharField(max_length=100, null=True)),
                ('front_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('particular_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('banks_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('buildings_and_lands_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('farms_and_enter_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('vehicles_and_household_items_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('spouse_children_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('bonds_shares_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('court_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('acknow_slip_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_1', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_2', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_3', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_4', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_5', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_6', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_7', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_8', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_9', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_10', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_11', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_12', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_13', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_14', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_15', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_16', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_17', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_18', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_19', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_20', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostEFCC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.CharField(max_length=100, null=True)),
                ('declarant_id', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('other_names', models.CharField(max_length=100, null=True)),
                ('date_ob', models.CharField(max_length=100, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('cadre', models.CharField(max_length=100, null=True)),
                ('rank_at_FAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_FAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_confirmation', models.CharField(max_length=100, null=True)),
                ('rank_at_LAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_LAPPT', models.CharField(max_length=100, null=True)),
                ('rank_at_PAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_PAPPT', models.CharField(max_length=100, null=True)),
                ('Num_Of_YIS', models.CharField(max_length=100, null=True)),
                ('Num_Of_YPIS', models.CharField(max_length=100, null=True)),
                ('date_OR', models.CharField(max_length=100, null=True)),
                ('date_of_1st_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_2nd_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_3rd_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_4th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_5th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_6th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_7th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_8th_declaration', models.CharField(max_length=100, null=True)),
                ('date_of_9th_declaration', models.CharField(max_length=100, null=True)),
                ('action_taken', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('investigation_activities', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('envelop_number', models.CharField(max_length=100, null=True)),
                ('box_number', models.CharField(max_length=100, null=True)),
                ('front_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('particular_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('banks_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('buildings_and_lands_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('farms_and_enter_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('vehicles_and_household_items_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('spouse_children_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('bonds_shares_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('court_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('acknow_slip_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_1', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_2', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_3', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_4', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_5', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_6', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_7', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_8', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_9', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_10', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_11', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_12', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_13', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_14', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_15', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_16', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_17', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_18', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_19', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('add_img_20', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostCCB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.CharField(max_length=100, null=True)),
                ('declarant_id', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('other_names', models.CharField(max_length=100, null=True)),
                ('date_ob', models.CharField(max_length=100, null=True)),
                ('year_FAPPT', models.IntegerField(blank=True, null=True)),
                ('year_ob', models.IntegerField(blank=True, null=True)),
                ('age_at_fa', models.IntegerField(blank=True, null=True)),
                ('retiring_at_35', models.CharField(max_length=100, null=True)),
                ('retiring_at_60', models.CharField(max_length=100, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('cadre', models.CharField(max_length=100, null=True)),
                ('rank_at_FAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_FAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_confirmation', models.CharField(max_length=100, null=True)),
                ('rank_at_LAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_LAPPT', models.CharField(max_length=100, null=True)),
                ('rank_at_PAPPT', models.CharField(max_length=100, null=True)),
                ('date_of_PAPPT', models.CharField(max_length=100, null=True)),
                ('Num_Of_YIS', models.IntegerField(blank=True, null=True)),
                ('curr_year', models.IntegerField(blank=True, null=True)),
                ('Num_Of_YPIS', models.IntegerField(blank=True, null=True)),
                ('year_OR', models.IntegerField(blank=True, null=True)),
                ('age_OR', models.IntegerField(blank=True, null=True)),
                ('date_OR', models.CharField(max_length=100, null=True)),
                ('date_of_1st_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_2nd_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_3rd_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_4th_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_5th_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_6th_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_7th_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_8th_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_9th_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('Num_Of_Times_To_declare', models.IntegerField(blank=True, null=True)),
                ('Num_Of_Times_declared', models.IntegerField(blank=True, null=True)),
                ('Num_Of_Times_defaulted', models.IntegerField(blank=True, null=True)),
                ('Year_Of_Next_declaration', models.IntegerField(blank=True, null=True)),
                ('action_taken', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('investigation_activities', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('envelop_number', models.CharField(max_length=100, null=True)),
                ('box_number', models.CharField(max_length=100, null=True)),
                ('front_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('particular_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('banks_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('buildings_and_lands_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('farms_and_enter_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('vehicles_and_household_items_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('spouse_children_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('bonds_shares_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('court_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('acknow_slip_img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_1', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_2', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_3', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_4', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_5', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_6', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_7', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_8', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_9', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('add_img_10', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_11', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_12', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_13', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_14', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_15', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_16', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_17', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_18', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_19', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('add_img_20', models.ImageField(blank=True, default='', null=True, upload_to='pics')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]