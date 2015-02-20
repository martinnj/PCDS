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
    publications = [] # a List of Publications
    positions = []
    skills = []
    educations = []
    courses = []

class Course(object):
    id  = "" 
    name   = "" 
    number  = "" 

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

class Company(object):
    id = ""
    name = ""
    type = "" 
    ticker = ""

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

file = open('full_extraction_example.json')
for line in file:
    data = line

if(data[1] == "u"):
    json_data = ast.literal_eval(data)
else:
    json_data = json.loads(data)

def get(data, query):
    if(query in data):
        # print ("getting " + query + " with value " + str(data[query]) + " and type "  + str(type(data[query])))
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
               exec("person.%s.append(classInstance)" % var)
        elif(var == "positions"):
           for position in getSub(data,"positions"):
               classInstance = createSub(var, Position, position) 
               exec("person.%s.append(classInstance)" % var)
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
        else: 
            exec("person.%s = \"%s\"" % (var, get(data,var)))
    return person
    
def createSub(name, className, data):
    variables = [s for s in dir(className) if s[0] != '_']
    classInstance = className()
    for var in variables:
        if(var[-4:] == "Date"):
            exec("classInstance.%s = \"%s\"" % (var, formatDate(get(data,var))))
        elif(var == "company"):
            classInstance.company = createSub(var, Company, get(data, var))
        elif(var == "name" and (name == "skills" or name == "publishers")):
            classInstance.name = data[name[:-1]][var]
        elif(var == "author"):
            classInstance.author = createSub(var, Author, get(data, var))
        else:
            exec("classInstance.%s = \"%s\"" % (var,get(data,var)))
        # exec()
        # exec("print \"%s is \" + str(classInstance.%s)" % (var, var))
    return classInstance

def formatDate(data):
    if data is "":
        return data
    return str(get(data,"month")) + "/" + str(get(data, "year"))

person = fillFullProfile(json_data)
# print person.courses[7].name
