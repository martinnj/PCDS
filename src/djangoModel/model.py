from django.db import models

class Person(models.Model):
    linkin_id = models.IntegerField()
    firstName =  models.CharField(max_length=30)
    maidenName = models.CharField(max_length=30)
    lastName =   models.CharField(max_length=30)
    headline = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    summary =  models.CharFiled(max_length=500)
    specialities = models.CharField(max_length=500)
    positions =    models.CharField(max_length=500)
    pictureUrl =   models.CharField(max_length=100)
    publicProfileUrl =models.CharField(max_length=100)
    formatted_name =  models.CharFiled(max_length=100)
    phoneticFirstName =     models.CharField(max_length=30)
    phoneticLastName =      models.CharField(max_length=30)
    formattedPhoneticName = models.CharField(max_length=30)

class Language(models.Model):
   lan_id = models.IntegerField()
   name = models.CharField(max_length = 30) 
   level = models.CharField(max_length = 30) 
   person = models.ForeignKey(Person) 

class Course(models.Model):
   cour_id  = models.IntegerField()
   name = models.CharField(max_length = 30) 
   number = models.CharField(max_length = 30) 
   person = models.ForeignKey(Person) 

class Skill(models.Model):
   skill_id = models.IntegerField()
   name = models.CharField(max_length = 30) 
   person = models.ForeignKey(Person) 

class Education(models.Model):
   edu_id = models.IntegerField()
   schoolName = models.CharField(max_length=200) 
   fieldOfStudy = models.CharField(max_length=200)
   startDate = models.DateField() 
   endDate = models.DateField() 
   degree = models.CharField(max_length=200)
   activities = models.CharField(max_length=500)
   notes = models.CharField(max_length=500)
   person = models.ForeignKey(Person) 

# class Position(models.Model):
   # # id = "" 
   # title = models.CharField(max_length = 100)
   # summary = models.CharField(max_length = 500) 
   # startDate = models.CharField(max_length = 10)
   # endDate = models.CharField(max_length = 10)
   # isCurrent = models.CharField(max_length = 10)
   # person = models.ForeignKey(Person) 
   # company = models.FOreignKey(Company)

# class Company(object):
   # # id = ""
   # name = models.CharField(max_length = 30) 
   # type = "" 
   # ticker = ""
   # position = models.ForeignKey(Position) 

# class Publication(object):
    # id = ""
    # title = ""
    # name = ""
    # date = ""
    # url = ""
    # summary = ""
    # author = ""

# class Author(object):
    # id = ""
    # name = ""
    # person = ""

# class Certification(object):
    # id = ""
    # name = ""
    # authority = ""
    # number = ""
    # startDate = ""
    # endDate = ""

