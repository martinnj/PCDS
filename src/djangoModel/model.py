from django.db import models

def insertPerson(p):
    person = Person(linkedin_id = int(person.id) ,firstname = p.firstName,
            maidenName = p.maidenName, lastName = p.lastName,
            headline = p.headline, location = p.location, industry = p.industry,
            summary = p.summary, specialities = p.specialities,
            positions = p.positions, pictureUrl = p.pictureUrl,
            publicProfileUrl = p.publicProfileUrl, formattedName =
            p.formattedName, phoneticFirstName = p.phoneticFirstName,
            phoneticLastName = p.phoneticLastName,
            formattedPhoneticName = p.formattedPhoneticName)
    p.save()

    for s in p.skills:
        ski = Skill(skill_id = int(s.id), name = s.name, person = p)
        ski.save()

    for l in p.languages:
        lang = Language(lan_id = int(l.id), name = l.name, level = l.Level,
                person = p)
        lang.save()

    for e in p.educations:
        edu = Education(edu_id = int(e.id), schoolname = e.schoolName,
                fieldOfStudy = e.fieldOfStudy, degree = e.degree,
                person = p)
        edu.save()

    for c in p.courses:
        cou = Course(cour_id = int(c.id), name = c.name, person = p)
        p.save()

class Person(models.Model):
    linkedin_id = models.IntegerField()
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
    formattedName =  models.CharFiled(max_length=100)
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
   person = models.ForeignKey(Person)

class Skill(models.Model):
   skill_id = models.IntegerField()
   name = models.CharField(max_length = 30)
   person = models.ForeignKey(Person)

class Education(models.Model):
   edu_id = models.IntegerField()
   schoolName = models.CharField(max_length=200)
   fieldOfStudy = models.CharField(max_length=200)
   degree = models.CharField(max_length=200)
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

