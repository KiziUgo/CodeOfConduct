from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.contenttypes.fields import GenericRelation
from PIL import Image
from ckeditor.fields import RichTextField
from django.shortcuts import render
from django.db.models import Q




class PostWelcome(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      declarant_id = models.CharField(null=True, max_length=100)
      date_posted = models.DateTimeField(null=True, auto_now_add=True)
      def __str__(self):
            return self.declarant_id

      def get_absolute_url(self):
            return reverse('postccb-create')


class PostCCBQuerySet(models.QuerySet):
      def search(self, query=None):
            qs = self
            if query is not None:
                  or_lookup = (Q(surname__icontains=query) |
                               Q(middle_name__icontains=query) |
                               Q(other_names__icontains=query)
                               )
                  qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
            return qs
class PostCCBManager(models.Manager):
      def get_queryset(self):
            return PostCCBQuerySet(self.model, using=self._db)
      def search(self, query=None):
            return self.get_queryset().search(query=query)


class PostCCB(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      file_number = models.CharField(null=True, max_length=100)
      declarant_id = models.CharField(null=True,max_length=100)
      date_posted = models.DateTimeField(null=True, auto_now_add=True)
      surname = models.CharField(null=True,max_length=100)
      middle_name = models.CharField(null=True,max_length=100)
      other_names = models.CharField(null=True,max_length=100)
      date_ob = models.CharField(null=True, max_length=100)
      year_FAPPT = models.IntegerField(null=True, blank=True)
      year_ob = models.IntegerField(null=True, blank=True)
      age_at_fa = models.IntegerField(null=True, blank=True)
      retiring_at_35 = models.CharField(null=True, max_length=100)
      retiring_at_60 = models.CharField(null=True, max_length=100)
      qualification = models.CharField(null=True, max_length=100)
      cadre = models.CharField(null=True, max_length=100)
      rank_at_FAPPT = models.CharField(null=True,max_length=100)
      date_of_FAPPT = models.CharField(null=True, max_length=100)
      date_of_confirmation = models.CharField(null=True, max_length=100)
      rank_at_LAPPT = models.CharField(null=True, max_length=100)
      date_of_LAPPT = models.CharField(null=True, max_length=100)
      rank_at_PAPPT = models.CharField(null=True, max_length=100)
      date_of_PAPPT = models.CharField(null=True, max_length=100)
      Num_Of_YIS = models.IntegerField(null=True, blank=True)
      curr_year = models.IntegerField(null=True, blank=True)
      Num_Of_YPIS = models.IntegerField(null=True, blank=True)
      year_OR = models.IntegerField(null=True, blank=True)
      age_OR = models.IntegerField(null=True, blank=True)
      date_OR = models.CharField(null=True, max_length=100)
      year_of_1st_declaration = models.IntegerField(null=True, blank=True)
      year_of_2nd_declaration = models.IntegerField(null=True, blank=True)
      year_of_3rd_declaration = models.IntegerField(null=True, blank=True)
      year_of_4th_declaration = models.IntegerField(null=True, blank=True)
      year_of_5th_declaration = models.IntegerField(null=True, blank=True)
      year_of_6th_declaration = models.IntegerField(null=True, blank=True)
      year_of_7th_declaration = models.IntegerField(null=True, blank=True)
      year_of_8th_declaration = models.IntegerField(null=True, blank=True)
      year_of_9th_declaration = models.IntegerField(null=True, blank=True)
      Num_Of_Times_To_declare = models.IntegerField(null=True, blank=True)
      Num_Of_Times_declared = models.IntegerField(null=True, blank=True)
      Num_Of_Times_defaulted = models.IntegerField(null=True, blank=True)
      Year_Of_Next_declaration = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare1 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare2 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare3 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare4 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare5 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare6 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare7 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare8 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare9 = models.IntegerField(null=True, blank=True)
      action_taken = RichTextField(blank=True, null=True)
      investigation_activities = RichTextField(blank=True, null=True)
      envelop_number = models.CharField(null=True, max_length=100)
      box_number = models.CharField(null=True, max_length=100)
      front_img = models.ImageField(null=True, blank=True, upload_to='pics')
      particular_img = models.ImageField(null=True, blank=True, upload_to='pics')
      banks_img = models.ImageField(null=True, blank=True, upload_to='pics')
      buildings_and_lands_img = models.ImageField(null=True, blank=True, upload_to='pics')
      farms_and_enter_img = models.ImageField(null=True, blank=True, upload_to='pics')
      vehicles_and_household_items_img = models.ImageField(null=True, blank=True, upload_to='pics')
      spouse_children_img = models.ImageField(null=True, blank=True, upload_to='pics')
      bonds_shares_img = models.ImageField(null=True, blank=True, upload_to='pics')
      court_img = models.ImageField(null=True, blank=True, upload_to='pics')
      acknow_slip_img = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_1 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_2 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_3 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_4 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_5 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_6 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_7 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_8 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_9 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_10 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_11 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_12 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_13 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_14 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_15 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_16 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_17 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_18 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_19 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_20 = models.ImageField(default='', null=True, blank=True, upload_to='pics')

      objects = PostCCBManager()

      def __str__(self):
            return self.declarant_id

      def save(self, *args, **kwargs):
            self.Num_Of_Times_declared = 0
            self.date_ob = self.date_ob.strip()
            self.year_ob = int(self.date_ob[-4:])
            self.date_of_FAPPT = self.date_of_FAPPT.strip()
            self.year_FAPPT = int(self.date_of_FAPPT[-4:])
            self.age_at_fa = self.year_FAPPT - self.year_ob
            if self.age_at_fa <= 24:
                  self.Num_Of_Times_To_declare = 9
                  self.retiring_at_35 = "Retiring at 35 Years of Service"
                  self.Num_Of_YIS = 35
                  self.var = 60 - self.age_at_fa
                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  self.Num_Of_Times_To_declare = 9
                  if self.Num_Of_Times_To_declare >= 10:
                        self.Num_Of_Times_To_declare = 9
                  else:
                        self.Num_Of_Times_To_declare = int(self.Num_Of_YIS / 4) + (self.Num_Of_YIS % 4 > 0)

                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  if self.year_of_1st_declaration == None:
                        self.year_of_1st_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1


                  if self.year_of_2nd_declaration == None:
                        self.year_of_2nd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_3rd_declaration == None:
                        self.year_of_3rd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_4th_declaration == None:
                        self.year_of_4th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_5th_declaration == None:
                        self.year_of_5th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_6th_declaration == None:
                        self.year_of_6th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_7th_declaration == None:
                        self.year_of_7th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_8th_declaration == None:
                        self.year_of_8th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_9th_declaration == None:
                        self.year_of_9th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  self.Num_Of_Times_defaulted = self.Num_Of_Times_To_declare - self.Num_Of_Times_declared

                  self.supposed_year_to_declare1 = self.year_FAPPT
                  self.supposed_year_to_declare2 = self.supposed_year_to_declare1 + 4
                  self.supposed_year_to_declare3 = self.supposed_year_to_declare2 + 4
                  self.supposed_year_to_declare4 = self.supposed_year_to_declare3 + 4
                  self.supposed_year_to_declare5 = self.supposed_year_to_declare4 + 4
                  self.supposed_year_to_declare6 = self.supposed_year_to_declare5 + 4
                  self.supposed_year_to_declare7 = self.supposed_year_to_declare6 + 4
                  self.supposed_year_to_declare8 = self.supposed_year_to_declare7 + 4
                  self.supposed_year_to_declare9 = self.supposed_year_to_declare8 + 4
            else:
                  self.retiring_at_60 = "Retiring at 60 Years of Age"
                  self.Num_Of_YIS = 60 - self.age_at_fa
                  self.Num_Of_Times_To_declare = 9
                  if self.Num_Of_Times_To_declare >= 10:
                        self.Num_Of_Times_To_declare = 9
                  else:
                        self.Num_Of_Times_To_declare = int(self.Num_Of_YIS / 4) + (self.Num_Of_YIS % 4 > 0)

                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  if self.year_of_1st_declaration == None:
                     self.year_of_1st_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1

                  if self.year_of_2nd_declaration == None:
                        self.year_of_2nd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_3rd_declaration == None:
                        self.year_of_3rd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_4th_declaration == None:
                        self.year_of_4th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_5th_declaration == None:
                        self.year_of_5th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_6th_declaration == None:
                        self.year_of_6th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_7th_declaration == None:
                        self.year_of_7th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_8th_declaration == None:
                        self.year_of_8th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_9th_declaration == None:
                        self.year_of_9th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  self.Num_Of_Times_defaulted = self.Num_Of_Times_To_declare - self.Num_Of_Times_declared

                  self.supposed_year_to_declare1 = self.year_FAPPT
                  self.supposed_year_to_declare2 = self.supposed_year_to_declare1 + 4
                  self.supposed_year_to_declare3 = self.supposed_year_to_declare2 + 4
                  self.supposed_year_to_declare4 = self.supposed_year_to_declare3 + 4
                  self.supposed_year_to_declare5 = self.supposed_year_to_declare4 + 4
                  self.supposed_year_to_declare6 = self.supposed_year_to_declare5 + 4
                  self.supposed_year_to_declare7 = self.supposed_year_to_declare6 + 4
                  self.supposed_year_to_declare8 = self.supposed_year_to_declare7 + 4
                  self.supposed_year_to_declare9 = self.supposed_year_to_declare8 + 4

            super().save(*args, **kwargs)



      def get_absolute_url(self):
            return reverse('ccbpost-detail', kwargs={'pk': self.pk})

class RegisterCCB(models.Model):
      declarant_ID = models.CharField(null=True, max_length=100)
      date_posted = models.DateTimeField(null=True, auto_now_add=True)
      name = models.CharField(null=True, max_length=100)
      rank = models.CharField(null=True, max_length=100)
      date_issued = models.CharField(null=True, max_length=100)
      date_sworn_to = models.CharField(null=True, max_length=100)
      date_recieved = models.CharField(null=True, max_length=100)
      def __str__(self):
            return self.declarant_ID

      def get_absolute_url(self):
            return reverse('postccb-create')


class PostEFCCQuerySet(models.QuerySet):
      def search(self, query=None):
            qs = self
            if query is not None:
                  or_lookup = (Q(surname__icontains=query) |
                               Q(middle_name__icontains=query) |
                               Q(other_names__icontains=query)
                               )
                  qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
            return qs
class PostEFCCManager(models.Manager):
      def get_queryset(self):
            return PostEFCCQuerySet(self.model, using=self._db)
      def search(self, query=None):
            return self.get_queryset().search(query=query)


class PostEFCC(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      file_number = models.CharField(null=True, max_length=100)
      declarant_id = models.CharField(null=True, max_length=100)
      date_posted = models.DateTimeField(null=True, auto_now_add=True)
      surname = models.CharField(null=True, max_length=100)
      middle_name = models.CharField(null=True, max_length=100)
      other_names = models.CharField(null=True, max_length=100)
      date_ob = models.CharField(null=True, max_length=100)
      year_FAPPT = models.IntegerField(null=True, blank=True)
      year_ob = models.IntegerField(null=True, blank=True)
      age_at_fa = models.IntegerField(null=True, blank=True)
      retiring_at_35 = models.CharField(null=True, max_length=100)
      retiring_at_60 = models.CharField(null=True, max_length=100)
      qualification = models.CharField(null=True, max_length=100)
      cadre = models.CharField(null=True, max_length=100)
      rank_at_FAPPT = models.CharField(null=True, max_length=100)
      date_of_FAPPT = models.CharField(null=True, max_length=100)
      date_of_confirmation = models.CharField(null=True, max_length=100)
      rank_at_LAPPT = models.CharField(null=True, max_length=100)
      date_of_LAPPT = models.CharField(null=True, max_length=100)
      rank_at_PAPPT = models.CharField(null=True, max_length=100)
      date_of_PAPPT = models.CharField(null=True, max_length=100)
      Num_Of_YIS = models.IntegerField(null=True, blank=True)
      curr_year = models.IntegerField(null=True, blank=True)
      Num_Of_YPIS = models.IntegerField(null=True, blank=True)
      year_OR = models.IntegerField(null=True, blank=True)
      age_OR = models.IntegerField(null=True, blank=True)
      date_OR = models.CharField(null=True, max_length=100)
      year_of_1st_declaration = models.IntegerField(null=True, blank=True)
      year_of_2nd_declaration = models.IntegerField(null=True, blank=True)
      year_of_3rd_declaration = models.IntegerField(null=True, blank=True)
      year_of_4th_declaration = models.IntegerField(null=True, blank=True)
      year_of_5th_declaration = models.IntegerField(null=True, blank=True)
      year_of_6th_declaration = models.IntegerField(null=True, blank=True)
      year_of_7th_declaration = models.IntegerField(null=True, blank=True)
      year_of_8th_declaration = models.IntegerField(null=True, blank=True)
      year_of_9th_declaration = models.IntegerField(null=True, blank=True)
      Num_Of_Times_To_declare = models.IntegerField(null=True, blank=True)
      Num_Of_Times_declared = models.IntegerField(null=True, blank=True)
      Num_Of_Times_defaulted = models.IntegerField(null=True, blank=True)
      Year_Of_Next_declaration = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare1 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare2 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare3 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare4 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare5 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare6 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare7 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare8 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare9 = models.IntegerField(null=True, blank=True)
      action_taken = RichTextField(blank=True, null=True)
      investigation_activities = RichTextField(blank=True, null=True)
      envelop_number = models.CharField(null=True, max_length=100)
      box_number = models.CharField(null=True, max_length=100)
      front_img = models.ImageField(null=True, blank=True, upload_to='pics')
      particular_img = models.ImageField(null=True, blank=True, upload_to='pics')
      banks_img = models.ImageField(null=True, blank=True, upload_to='pics')
      buildings_and_lands_img = models.ImageField(null=True, blank=True, upload_to='pics')
      farms_and_enter_img = models.ImageField(null=True, blank=True, upload_to='pics')
      vehicles_and_household_items_img = models.ImageField(null=True, blank=True, upload_to='pics')
      spouse_children_img = models.ImageField(null=True, blank=True, upload_to='pics')
      bonds_shares_img = models.ImageField(null=True, blank=True, upload_to='pics')
      court_img = models.ImageField(null=True, blank=True, upload_to='pics')
      acknow_slip_img = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_1 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_2 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_3 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_4 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_5 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_6 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_7 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_8 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_9 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_10 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_11 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_12 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_13 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_14 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_15 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_16 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_17 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_18 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_19 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_20 = models.ImageField(default='', null=True, blank=True, upload_to='pics')

      objects = PostEFCCManager()

      def __str__(self):
            return self.declarant_id

      def save(self, *args, **kwargs):
            self.Num_Of_Times_declared = 0
            self.date_ob = self.date_ob.strip()
            self.year_ob = int(self.date_ob[-4:])
            self.date_of_FAPPT = self.date_of_FAPPT.strip()
            self.year_FAPPT = int(self.date_of_FAPPT[-4:])
            self.age_at_fa = self.year_FAPPT - self.year_ob
            if self.age_at_fa <= 24:
                  self.Num_Of_Times_To_declare = 9
                  self.retiring_at_35 = "Retiring at 35 Years of Service"
                  self.Num_Of_YIS = 35
                  self.var = 60 - self.age_at_fa
                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  self.Num_Of_Times_To_declare = 9
                  if self.Num_Of_Times_To_declare >= 10:
                        self.Num_Of_Times_To_declare = 9
                  else:
                        self.Num_Of_Times_To_declare = int(self.Num_Of_YIS / 4) + (self.Num_Of_YIS % 4 > 0)

                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  if self.year_of_1st_declaration == None:
                        self.year_of_1st_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1

                  if self.year_of_2nd_declaration == None:
                        self.year_of_2nd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_3rd_declaration == None:
                        self.year_of_3rd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_4th_declaration == None:
                        self.year_of_4th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_5th_declaration == None:
                        self.year_of_5th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_6th_declaration == None:
                        self.year_of_6th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_7th_declaration == None:
                        self.year_of_7th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_8th_declaration == None:
                        self.year_of_8th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_9th_declaration == None:
                        self.year_of_9th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  self.Num_Of_Times_defaulted = self.Num_Of_Times_To_declare - self.Num_Of_Times_declared

                  self.supposed_year_to_declare1 = self.year_FAPPT
                  self.supposed_year_to_declare2 = self.supposed_year_to_declare1 + 4
                  self.supposed_year_to_declare3 = self.supposed_year_to_declare2 + 4
                  self.supposed_year_to_declare4 = self.supposed_year_to_declare3 + 4
                  self.supposed_year_to_declare5 = self.supposed_year_to_declare4 + 4
                  self.supposed_year_to_declare6 = self.supposed_year_to_declare5 + 4
                  self.supposed_year_to_declare7 = self.supposed_year_to_declare6 + 4
                  self.supposed_year_to_declare8 = self.supposed_year_to_declare7 + 4
                  self.supposed_year_to_declare9 = self.supposed_year_to_declare8 + 4
            else:
                  self.retiring_at_60 = "Retiring at 60 Years of Age"
                  self.Num_Of_YIS = 60 - self.age_at_fa
                  self.Num_Of_Times_To_declare = 9
                  if self.Num_Of_Times_To_declare >= 10:
                        self.Num_Of_Times_To_declare = 9
                  else:
                        self.Num_Of_Times_To_declare = int(self.Num_Of_YIS / 4) + (self.Num_Of_YIS % 4 > 0)

                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  if self.year_of_1st_declaration == None:
                        self.year_of_1st_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1

                  if self.year_of_2nd_declaration == None:
                        self.year_of_2nd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_3rd_declaration == None:
                        self.year_of_3rd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_4th_declaration == None:
                        self.year_of_4th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_5th_declaration == None:
                        self.year_of_5th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_6th_declaration == None:
                        self.year_of_6th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_7th_declaration == None:
                        self.year_of_7th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_8th_declaration == None:
                        self.year_of_8th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_9th_declaration == None:
                        self.year_of_9th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  self.Num_Of_Times_defaulted = self.Num_Of_Times_To_declare - self.Num_Of_Times_declared

                  self.supposed_year_to_declare1 = self.year_FAPPT
                  self.supposed_year_to_declare2 = self.supposed_year_to_declare1 + 4
                  self.supposed_year_to_declare3 = self.supposed_year_to_declare2 + 4
                  self.supposed_year_to_declare4 = self.supposed_year_to_declare3 + 4
                  self.supposed_year_to_declare5 = self.supposed_year_to_declare4 + 4
                  self.supposed_year_to_declare6 = self.supposed_year_to_declare5 + 4
                  self.supposed_year_to_declare7 = self.supposed_year_to_declare6 + 4
                  self.supposed_year_to_declare8 = self.supposed_year_to_declare7 + 4
                  self.supposed_year_to_declare9 = self.supposed_year_to_declare8 + 4

            super().save(*args, **kwargs)


      def get_absolute_url(self):
            return reverse('efccpost-detail', kwargs={'pk': self.pk})


class RegisterEFCC(models.Model):
      declarant_ID = models.CharField(null=True, max_length=100)
      date_posted = models.DateTimeField(null=True, auto_now_add=True)
      name = models.CharField(null=True, max_length=100)
      rank = models.CharField(null=True, max_length=100)
      date_issued = models.CharField(null=True, max_length=100)
      date_sworn_to = models.CharField(null=True, max_length=100)
      date_recieved = models.CharField(null=True, max_length=100)
      def __str__(self):
            return self.declarant_ID

      def get_absolute_url(self):
            return reverse('postefcc-create')



class PostICPCQuerySet(models.QuerySet):
      def search(self, query=None):
            qs = self
            if query is not None:
                  or_lookup = (Q(surname__icontains=query) |
                               Q(middle_name__icontains=query) |
                               Q(other_names__icontains=query)
                               )
                  qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
            return qs
class PostICPCManager(models.Manager):
      def get_queryset(self):
            return PostICPCQuerySet(self.model, using=self._db)
      def search(self, query=None):
            return self.get_queryset().search(query=query)


class PostICPC(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      file_number = models.CharField(null=True, max_length=100)
      declarant_id = models.CharField(null=True, max_length=100)
      date_posted = models.DateTimeField(null=True, auto_now_add=True)
      surname = models.CharField(null=True, max_length=100)
      middle_name = models.CharField(null=True, max_length=100)
      other_names = models.CharField(null=True, max_length=100)
      date_ob = models.CharField(null=True, max_length=100)
      year_FAPPT = models.IntegerField(null=True, blank=True)
      year_ob = models.IntegerField(null=True, blank=True)
      age_at_fa = models.IntegerField(null=True, blank=True)
      retiring_at_35 = models.CharField(null=True, max_length=100)
      retiring_at_60 = models.CharField(null=True, max_length=100)
      qualification = models.CharField(null=True, max_length=100)
      cadre = models.CharField(null=True, max_length=100)
      rank_at_FAPPT = models.CharField(null=True, max_length=100)
      date_of_FAPPT = models.CharField(null=True, max_length=100)
      date_of_confirmation = models.CharField(null=True, max_length=100)
      rank_at_LAPPT = models.CharField(null=True, max_length=100)
      date_of_LAPPT = models.CharField(null=True, max_length=100)
      rank_at_PAPPT = models.CharField(null=True, max_length=100)
      date_of_PAPPT = models.CharField(null=True, max_length=100)
      Num_Of_YIS = models.IntegerField(null=True, blank=True)
      curr_year = models.IntegerField(null=True, blank=True)
      Num_Of_YPIS = models.IntegerField(null=True, blank=True)
      year_OR = models.IntegerField(null=True, blank=True)
      age_OR = models.IntegerField(null=True, blank=True)
      date_OR = models.CharField(null=True, max_length=100)
      year_of_1st_declaration = models.IntegerField(null=True, blank=True)
      year_of_2nd_declaration = models.IntegerField(null=True, blank=True)
      year_of_3rd_declaration = models.IntegerField(null=True, blank=True)
      year_of_4th_declaration = models.IntegerField(null=True, blank=True)
      year_of_5th_declaration = models.IntegerField(null=True, blank=True)
      year_of_6th_declaration = models.IntegerField(null=True, blank=True)
      year_of_7th_declaration = models.IntegerField(null=True, blank=True)
      year_of_8th_declaration = models.IntegerField(null=True, blank=True)
      year_of_9th_declaration = models.IntegerField(null=True, blank=True)
      Num_Of_Times_To_declare = models.IntegerField(null=True, blank=True)
      Num_Of_Times_declared = models.IntegerField(null=True, blank=True)
      Num_Of_Times_defaulted = models.IntegerField(null=True, blank=True)
      Year_Of_Next_declaration = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare1 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare2 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare3 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare4 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare5 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare6 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare7 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare8 = models.IntegerField(null=True, blank=True)
      supposed_year_to_declare9 = models.IntegerField(null=True, blank=True)
      action_taken = RichTextField(blank=True, null=True)
      investigation_activities = RichTextField(blank=True, null=True)
      envelop_number = models.CharField(null=True, max_length=100)
      box_number = models.CharField(null=True, max_length=100)
      front_img = models.ImageField(null=True, blank=True, upload_to='pics')
      particular_img = models.ImageField(null=True, blank=True, upload_to='pics')
      banks_img = models.ImageField(null=True, blank=True, upload_to='pics')
      buildings_and_lands_img = models.ImageField(null=True, blank=True, upload_to='pics')
      farms_and_enter_img = models.ImageField(null=True, blank=True, upload_to='pics')
      vehicles_and_household_items_img = models.ImageField(null=True, blank=True, upload_to='pics')
      spouse_children_img = models.ImageField(null=True, blank=True, upload_to='pics')
      bonds_shares_img = models.ImageField(null=True, blank=True, upload_to='pics')
      court_img = models.ImageField(null=True, blank=True, upload_to='pics')
      acknow_slip_img = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_1 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_2 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_3 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_4 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_5 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_6 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_7 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_8 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_9 = models.ImageField(null=True, blank=True, upload_to='pics')
      add_img_10 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_11 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_12 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_13 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_14 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_15 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_16 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_17 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_18 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_19 = models.ImageField(default='', null=True, blank=True, upload_to='pics')
      add_img_20 = models.ImageField(default='', null=True, blank=True, upload_to='pics')

      objects = PostICPCManager()

      def __str__(self):
            return self.declarant_id

      def save(self, *args, **kwargs):
            self.Num_Of_Times_declared = 0
            self.date_ob = self.date_ob.strip()
            self.year_ob = int(self.date_ob[-4:])
            self.date_of_FAPPT = self.date_of_FAPPT.strip()
            self.year_FAPPT = int(self.date_of_FAPPT[-4:])
            self.age_at_fa = self.year_FAPPT - self.year_ob
            if self.age_at_fa <= 24:
                  self.Num_Of_Times_To_declare = 9
                  self.retiring_at_35 = "Retiring at 35 Years of Service"
                  self.Num_Of_YIS = 35
                  self.var = 60 - self.age_at_fa
                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  self.Num_Of_Times_To_declare = 9
                  if self.Num_Of_Times_To_declare >= 10:
                        self.Num_Of_Times_To_declare = 9
                  else:
                        self.Num_Of_Times_To_declare = int(self.Num_Of_YIS / 4) + (self.Num_Of_YIS % 4 > 0)

                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  if self.year_of_1st_declaration == None:
                        self.year_of_1st_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1

                  if self.year_of_2nd_declaration == None:
                        self.year_of_2nd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_3rd_declaration == None:
                        self.year_of_3rd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_4th_declaration == None:
                        self.year_of_4th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_5th_declaration == None:
                        self.year_of_5th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_6th_declaration == None:
                        self.year_of_6th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_7th_declaration == None:
                        self.year_of_7th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_8th_declaration == None:
                        self.year_of_8th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_9th_declaration == None:
                        self.year_of_9th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  self.Num_Of_Times_defaulted = self.Num_Of_Times_To_declare - self.Num_Of_Times_declared

                  self.supposed_year_to_declare1 = self.year_FAPPT
                  self.supposed_year_to_declare2 = self.supposed_year_to_declare1 + 4
                  self.supposed_year_to_declare3 = self.supposed_year_to_declare2 + 4
                  self.supposed_year_to_declare4 = self.supposed_year_to_declare3 + 4
                  self.supposed_year_to_declare5 = self.supposed_year_to_declare4 + 4
                  self.supposed_year_to_declare6 = self.supposed_year_to_declare5 + 4
                  self.supposed_year_to_declare7 = self.supposed_year_to_declare6 + 4
                  self.supposed_year_to_declare8 = self.supposed_year_to_declare7 + 4
                  self.supposed_year_to_declare9 = self.supposed_year_to_declare8 + 4
            else:
                  self.retiring_at_60 = "Retiring at 60 Years of Age"
                  self.Num_Of_YIS = 60 - self.age_at_fa
                  self.Num_Of_Times_To_declare = 9
                  if self.Num_Of_Times_To_declare >= 10:
                        self.Num_Of_Times_To_declare = 9
                  else:
                        self.Num_Of_Times_To_declare = int(self.Num_Of_YIS / 4) + (self.Num_Of_YIS % 4 > 0)

                  self.Num_Of_YPIS = self.curr_year - self.year_FAPPT
                  self.year_OR = self.year_FAPPT + self.Num_Of_YIS
                  self.age_OR = self.age_at_fa + self.Num_Of_YIS

                  if self.year_of_1st_declaration == None:
                        self.year_of_1st_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1

                  if self.year_of_2nd_declaration == None:
                        self.year_of_2nd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_3rd_declaration == None:
                        self.year_of_3rd_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_4th_declaration == None:
                        self.year_of_4th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_5th_declaration == None:
                        self.year_of_5th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_6th_declaration == None:
                        self.year_of_6th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_7th_declaration == None:
                        self.year_of_7th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_8th_declaration == None:
                        self.year_of_8th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  if self.year_of_9th_declaration == None:
                        self.year_of_9th_declaration = 0
                  else:
                        self.Num_Of_Times_declared += 1
                  self.Num_Of_Times_defaulted = self.Num_Of_Times_To_declare - self.Num_Of_Times_declared

                  self.supposed_year_to_declare1 = self.year_FAPPT
                  self.supposed_year_to_declare2 = self.supposed_year_to_declare1 + 4
                  self.supposed_year_to_declare3 = self.supposed_year_to_declare2 + 4
                  self.supposed_year_to_declare4 = self.supposed_year_to_declare3 + 4
                  self.supposed_year_to_declare5 = self.supposed_year_to_declare4 + 4
                  self.supposed_year_to_declare6 = self.supposed_year_to_declare5 + 4
                  self.supposed_year_to_declare7 = self.supposed_year_to_declare6 + 4
                  self.supposed_year_to_declare8 = self.supposed_year_to_declare7 + 4
                  self.supposed_year_to_declare9 = self.supposed_year_to_declare8 + 4

            super().save(*args, **kwargs)


      def get_absolute_url(self):
            return reverse('icpcpost-detail', kwargs={'pk': self.pk})


class RegisterICPC(models.Model):
      declarant_ID = models.CharField(null=True, max_length=100)
      date_posted = models.DateTimeField(null=True, auto_now_add=True)
      name = models.CharField(null=True, max_length=100)
      rank = models.CharField(null=True, max_length=100)
      date_issued = models.CharField(null=True, max_length=100)
      date_sworn_to = models.CharField(null=True, max_length=100)
      date_recieved = models.CharField(null=True, max_length=100)
      def __str__(self):
            return self.declarant_ID

      def get_absolute_url(self):
            return reverse('posticpc-create')
























