#Python base packages
import uuid
import StringIO
import re
import os
import logging

# Django packages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import models
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile

# Lord knows what packages :P
from PIL import Image as Img
from rest_framework.reverse import reverse

# Apps packages and leapkit stuff.
from institutions.models import Institution, Department, Course, FieldOfStudy
from geographic_info.models import City, Region, ZipCode, Street, Country
from projects.models import Project
from leapkit import settings

# LinkedIn conversion.
from students.linkedin_converter import fromString

class LinkedInProfile(models.Model):

    """
    This model is used to represent a students LinkedIn information.
    """
    # The userid/link to a specific user
    leapkituser = models.OneToOneField(User)

    # Last time the data was modified/updated.
    modified = models.DateTimeField('modified', auto_now=True)

    # Profile ID from linkedIn.
    linkedin_id = models.TextField()

    # Name information from LinkedIn
    firstName =  models.TextField()
    lastName = models.TextField()

    # Misc information from LinkedIn
    pictureUrl = models.TextField(null=True, blank=True)
    publicProfileUrl = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        :return: First name + last name, with a space in between
        """
        return "%s %s" % (self.firstName, self.lastName)

class Language(models.Model):
   name = models.CharField(max_length = 30)
   level = models.CharField(max_length = 30)
   profile = models.ForeignKey(LinkedInProfile)

   def __unicode__(self):
       return self.get_language()

   def get_language(self):
       return "%s" % (self.name)

class Course(models.Model):
   name = models.CharField(max_length = 81)
   profile = models.ForeignKey(LinkedInProfile)

   def __unicode__(self):
       return self.get_course()

   def get_course(self):
       return "%s" % (self.name)

class Skill(models.Model):
   name = models.CharField(max_length = 81)
   profile = models.ForeignKey(LinkedInProfile)

   def __unicode__(self):
       return self.get_skill()

   def get_skill(self):
       return "%s" % (self.name)

class Education(models.Model):
   schoolName = models.CharField(max_length=100)
   fieldOfStudy = models.CharField(max_length=100)
   degree = models.CharField(max_length=100)
   profile = models.ForeignKey(LinkedInProfile)

   def __unicode__(self):
       return self.get_fieldOfStudy()

   def get_fieldOfStudy(self):
       return "%s" % (self.fieldOfStudy)

class Position(models.Model):
   startDate = models.CharField(max_length=20)
   endDate = models.CharField(max_length=20)
   company = models.CharField(max_length=100)
   jobtitle = models.CharField(max_length=100)
   isCurrent = models.BooleanField(default=False)
   profile = models.ForeignKey(LinkedInProfile)

   def __unicode__(self):
       return self.get_jobtitle()

   def get_jobtitle(self):
       return "%s" % (self.jobtitle)

def insertLinkedInProfile(p_json, LeapkitUsername):
  """
  Reads a JSON string and enters the information into the database.
  If the user already exists it gets the data updated.

  TODO: Implement all or nothing semantics.
  """
    p = fromString(p_json) # Converts json data to the 'desired' structure

    user = User.objects.get(username=LeapkitUsername)
    """Checks if linkedin data already exists"""
    if LinkedInProfile.objects.filter(leapkituser = user):
        """If exists, profile is updated"""
        profile = LinkedInProfile.objects.get(leapkituser=user)
        profile.__dict__.update(linkedin_id = p.pid,
                                  firstName = p.firstName,
                                  lastName = p.lastName,
                                  pictureUrl = p.pictureUrl,
                                  publicProfileUrl = p.publicProfileUrl)

        """Seemed useful at the time"""
        try:
            Skill.objects.filter(profile=profile).delete()
        except:
            logging.error("Skills not deleted")
        try:
            Education.objects.filter(profile=profile).delete()
        except:
            logging.error("Education not deleted")
        try:
            Language.objects.filter(profile=profile).delete()
        except:
            logging.error("Language not deleted")
        try:
            Course.objects.filter(profile=profile).delete()
        except:
            logging.error("Course not deleted")
        try:
            Position.objects.filter(profile=profile).delete()
        except:
            logging.error("Position not deleted")

        for ps in p.positions:
            pos = Position(startDate = ps.startDate, endDate = ps.endDate,
                    company = ps.company, jobtitle = ps.title,
                    isCurrent = ps.isCurrent, profile = profile)
            pos.save()

        for s in p.skills:
            ski = Skill(name = s.name, profile = profile)
            ski.save()

        for l in p.languages:
            lang = Language(name = l.name, level = l.level,
                    profile = profile)
            lang.save()

        for e in p.educations:
            edu = Education(schoolName = e.schoolName,
                    fieldOfStudy = e.fieldOfStudy, degree = e.degree,
                    profile = profile)
            edu.save()

        for c in p.courses:
            cou = Course(name = c.name, profile = profile)
            cou.save()

    else:
        """Creates new LinkedInProfile"""
        profile = LinkedInProfile(leapkituser = user,
                                  linkedin_id = p.pid,
                                  firstName = p.firstName,
                                  lastName = p.lastName,
                                  pictureUrl = p.pictureUrl,
                                  publicProfileUrl = p.publicProfileUrl)
        profile.save()

        for ps in p.positions:
            pos = Position(startDate = ps.startDate, endDate = ps.endDate,
                    company = ps.company, jobtitle = ps.title,
                    isCurrent = ps.isCurrent, profile = profile)
            pos.save()

        for s in p.skills:
            ski = Skill(name = s.name, profile = profile)
            ski.save()

        for l in p.languages:
            lang = Language(name = l.name, level = l.level,
                    profile = profile)
            lang.save()

        for e in p.educations:
            edu = Education(schoolName = e.schoolName,
                    fieldOfStudy = e.fieldOfStudy, degree = e.degree,
                    profile = profile)
            edu.save()

        for c in p.courses:
            cou = Course(name = c.name, profile = profile)
            cou.save()
