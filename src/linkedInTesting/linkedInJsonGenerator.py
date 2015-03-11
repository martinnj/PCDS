import json
import string
import random
import testingLists as lists

def create(typeFunction, percentage, list):
    """Creates a list of elements from list and returns it. The percentage
       is how likely the method is to add another element from the list"""
    retDic = {"_total": 0, "values" : []}
    while(random.uniform(1,100) < percentage):
        typeFunction(retDic, list)
    return retDic

def addToDic(dic, element):
    """Adds the element to the dic and increments the counter _total"""
    dic["_total"] += 1
    dic["values"].append(element)

def skills(dic, skillsList):
    """Add a element from the skillsList to the dictornary dic"""
    (name, id) = getRand(skillsList)
    # Finds if the skill is a duplicate and
    # adds the element if it is not a duplicate
    if(not ignoreDuplicate(dic, id)):
        newIn = {"skill": {"name": name}, "id" : id}
        addToDic(dic, newIn)

def languages(dic, languageList):
    """Add a element from the languageList to the dictornary dic"""
    (name, id) = getRand(languageList)
    # Finds if the skill is a duplicate and
    # adds the element if it is not a duplicate
    if(not ignoreDuplicate(dic, id)):
        nameIns = {"name" : name}
        newIn = {"id": id, "language": nameIns}
        addToDic(dic, newIn)

def ignoreDuplicate(dic, id):
    """finds if the element is a duplicate"""
    isDuplicate = False
    for element in dic["values"]:
        if id == element["id"]:
            isDuplicate = True
    return isDuplicate

def getRand(list):
    """Returns a random element of list"""
    return(list[random.randint(0,len(list)-1)])

def randomWord():
    """Generates a random 6 letter String with all caps"""
    return ''.join(random.choice(string.ascii_uppercase) for i in range(6))

def names():
    """Generates a first, maiden and last name"""
    return (randomWord(), randomWord(), randomWord())

def generate(genLists):
    """The method to call.
        Generates a random json file in LinkedIn format.
        Returns a tuple with the path of the file, and the json as
        a string. """
    skill = create(skills, 80, genLists[0])
    language = create(languages, 50, genLists[1])
    (first, maiden, last) = names()
    dic = {"skills" : skill, "languages" : language, "firstName" : first, 
           "maidenName" : maiden, "lastName" : last}
    return json.dumps(dic)

def writeTo(path, s):
    """Writes the String s into the file at path, returns the path and the
    string"""
    f = open(path, "w") 
    for line in s:
        f.write(line + "\n")
    f.close()
    return (path, s)

def main():
    # generateLists = True 
    generateLists = False
    # dirty = True
    dirty = False 
    amount = 1000

    genLists = []

    if generateLists:
        genLists.append(lists.generateSkills(dirty))
        genLists.append(lists.generateLanguages())
    else:
        genLists.append(lists.getSkills())
        genLists.append(lists.getLanguages())

    json = []
    for _ in range(amount):
        json.append(generate(genLists))
    # print json
    return writeTo("linkedInTesting/jsonGenerated.json", json)

if __name__ == "__main__":
    main()
