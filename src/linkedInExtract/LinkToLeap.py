import json
from pprint import pprint
import ast

class Person(object):
    id = ""
    firstName = ""
    maidenName = ""
    lastName = ""
    headline = ""
    location = ""
    industry = ""
    summary = ""
    specialities = ""
    positions = ""
    pictureUrl = ""
    publicProfileUrl = ""
    formatted_name = ""
    phoneticFirstName = ""
    phoneticLastName = ""
    formattedPhoneticName = ""
    #Lists
    publications = []
    positions = []
    skills = []
    educations = []
    courses = []
    languages = []

class Language(object):
   id = ""
   name = ""
   level = ""

class Course(object):
    id  = "" 
    name   = "" 
    number  = "" 
    def __str__(self):
        return "id = " + self.id + "\n  name = " + self.name + "\nnumber = " + number

class Skill(object):
    id = ""
    name = ""
    def __str__(self):
        return "id = " + self.id + ", name = " + self.name

class Position(object):
    id = "" 
    title = ""
    summary = ""
    startDate = ""
    endDate = ""
    isCurrent = ""
    company = "" 
    def __str__(self):
        ret  = "  id = " +        self.id +     "\n  title = " +     self.title 
        ret += "\n  summary = " + self.summary +"\n  startDate = " + self.startDate 
        ret += "\n  endDate = " + self.endDate +"\n  isCurrent = " + self.isCurrent 
        if (not self.company is ""):
            ret += "\n  company = " + self.company.__str__()
        else:
            ret += "\n  company = " + self.company
        return ret

class Company(object):
    id = ""
    name = ""
    type = "" 
    ticker = ""
    def __str__(self):
        return "\n    id = " + self.id + "\n    name = " + self.name + "\n    type = " + self.type + "\n    ticker = " + self.ticker


class Publication(object):
    id = ""
    title = ""
    name = ""
    date = ""
    url = ""
    summary = ""
    author = ""

class Author(object):
    id = ""
    name = ""
    person = ""

class Education(object):
    id = ""
    schoolName = ""
    fieldOfStudy = ""
    startDate = ""
    endDate = ""
    degree = ""
    activities = ""
    notes = ""

class Certification(object):
    id = ""
    name = ""
    authority = ""
    number = ""
    startDate = ""
    endDate = ""


def get(data, query):
    if(query in data):
        return data[query]
    else:
        return ""

def getSub(data, query):
    if("values" in get(data,query)):
        return get(data, query)["values"]
    else:
        return []

def fillFullProfile(data):
    variables = [s for s in dir(Person) if s[0] != '_']
    person = Person()
    for var in variables:
        if(var == "publications"):
            for publication in getSub(data, "publications"):
               classInstance = createSub(var, Publication, publication) 
               person.publications.append(classInstance)
        elif(var == "languages"):
           for language in getSub(data,"languages"):
               classInstance = createSub(var, Language, language) 
               person.languages.append(classInstance)
        elif(var == "positions"):
           for position in getSub(data,"positions"):
               classInstance = createSub(var, Position, position) 
               person.positions.append(classInstance)
        elif(var == "educations"):
           for education in getSub(data,"educations"):
               classInstance = createSub(var, Education, education) 
               person.educations.append(classInstance)
        elif(var == "skills"):
            for skill in getSub(data, "skills"):
               person.skills.append(createSub(var, Skill, skill))
        elif(var == "courses"):
            for course in getSub(data, "courses"):
               person.courses.append(createSub(var, Course, course))
        elif(var == "certifications"):
            for certification in getSub(data, "certifications"):
               person.certification.append(createSub(var, Certification, certification))
        else: 
            exec("person.%s = \"%s\"" % (var, get(data,var)))
    return person
    
def createSub(name, className, data):
    variables = [s for s in dir(className) if s[0] != '_']
    classInstance = className()
    for var in variables:
        if(var[-4:] == "Date"):
            exec("classInstance.%s = \"%s\"" % (var, formatDate(get(data,var))))
        elif var == "company" :
            classInstance.company = createSub(var, Company, get(data, var))
        elif var == "name" and name == "authorities":
            classInstance.authority = data[name[:-1]][var]
        elif(var == "name" and (name == "languages" or name == "skills" or name == "publishers")):
            classInstance.name = data[name[:-1]][var]
        elif(var == "level" and name == "languages"):
            classInstance.level = data["proficiency"][var]
        elif(var == "author"):
            classInstance.author = createSub(var, Author, get(data, var))
        else:
            exec("classInstance.%s = \"%s\"" % (var,get(data,var)))
    return classInstance

def formatDate(data):
    if data is "":
        return data
    return str(get(data,"month")) + "/" + str(get(data, "year"))

def run(rawdata):
    if(rawdata[1] == "u"):
        json_data = ast.literal_eval(rawdata)
    else:
        json_data = json.loads(rawdata)
    return fillFullProfile(json_data)

def fromFile(path):
    file = open(path)
    data = ""
    for line in file:
        data += line
    return run(data)

def fromString(data):
    return run(data)
