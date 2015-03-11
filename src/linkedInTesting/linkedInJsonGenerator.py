import json
import string
import random
import testingLists as lists

generate = True 
dirty = True



if generate:
    skillsList = lists.generateSkills(dirty)
    languageList = lists.generateLanguages()
else:
    skillsList = getSkills()
    languageList = getLanguages()

def create(typeFunction, percentage):
    retDic = {"_total": 0, "values" : []}
    while(random.uniform(1,100) < percentage):
        typeFunction(retDic)
    return retDic

def skills(dic):
    isDuplicate = False
    (name, id) = getRand(skillsList)
    # Finds if the skill is a duplicate
    for element in dic["values"]:
        if id == element["id"]:
            isDuplicate = True
    # Adds the element if it is not a duplicate
    if(not isDuplicate):
        newIn = {"skill": {"name": name}, "id" : id}
        dic["_total"] += 1
        dic["values"].append(newIn)

def languages(dic):
    isDuplicate = False
    (name, id) = getRand(languageList)
    # Finds if the skill is a duplicate
    for element in dic["values"]:
        # print element
        if id == element["id"]:
            isDuplicate = True
    # Adds the element if it is not a duplicate
    if(not isDuplicate):
        nameIns = {"name" : name}
        newIn = {"id": id, "language": nameIns}
        dic["_total"] += 1
        dic["values"].append(newIn)

def getRand(list):
    return(list[random.randint(0,len(list)-1)])

def randomWord():
    return ''.join(random.choice(string.ascii_uppercase) for i in range(6))

def names():
    return (randomWord(), randomWord(), randomWord())

def generate():
    skill = create(skills, 85)
    language = create(languages, 45)
    (first, maiden, last) = names()
    # print names()
    dic = {"skills" : skill, "languages" : language, "firstName" : first, 
           "maidenName" : maiden, "lastName" : last}
    return writeTo("linkedInTesting/jsonGenerated.json", json.dumps(dic))
    # return json.dumps(dic)

def writeTo(path, s):
    f = open(path, "w") 
    f.write(s)
    f.close()
    return path
# print json.dumps(create(skills, 85))
# print json.dumps(create(languages, 45))
# print generate()
