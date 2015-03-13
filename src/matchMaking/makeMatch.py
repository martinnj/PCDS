


#Returns the degree of match between the given array of source and target skills.
#Returns -1 if skills empty.
#Takes a compare function compareFun, which takes a single skill and a target 
#list of skills. It must return 1 if skill match target skills, otherwise 0.
#Expects sourceSkills and targetSkills to be lists of strings.
def matchSkills(sourceSkills, targetSkills, compareFun):
    #Clear for empty strings and test for empty lists.
    emptyString = ""
    while emptyString in sourceSkills:
        sourceSkills.remove(emptyString) 
    while emptyString in targetSkills:
        targetSkills.remove(emptyString) 

    if not sourceSkills or not targetSkills:
        return -1

    #Match skills.
    matchSum = 0
    for skill in sourceSkills:
        matchSum += compareFun(skill, targetSkills)

    return matchSum / len(sourceSkills)


#Returns 1 if string is equal to a string in stringList, otherwise 0.
def strictCompare(string, stringList):
    return any(string.lower() == s.lower() for s in stringList)

#Returns 1 if string is contained in a string in stringList, otherwise 0.
#Note: boolean values False and True are considered to be 0 and 1, respectively,
#except when converted to string.
def containsStringCompare(string, stringList):
    return any(string.lower() in s.lower()  for s in stringList)