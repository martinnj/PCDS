#!/bin/env python2

#import operator

############### HELPER METHODS ###############

#Returns the degree of match between the given list of source and target 
#strings.
#Returns -1 if any list is empty.
#Takes a compare function compareFun, which takes a single string s and a target 
#list l of strings s_i. It must return 1 if s matches any target string s_i, 
#otherwise 0.
def matchListsOfStrings(sourceList, targetList, compareFun):
    #Clear for empty strings and test for empty lists.
    emptyString = ""
    while emptyString in sourceList:
        sourceList.remove(emptyString) 
    while emptyString in targetList:
        targetList.remove(emptyString)

    if not sourceList or not targetList:
        return -1

    #Match skills.
    matchSum = 0
    for skill in sourceList:
        matchSum += compareFun(skill, targetList)

    return matchSum / len(sourceList)




#Returns 1 if string is equal to a string in stringList, otherwise 0.
def strictCompare(string, stringList):
    return any(string.lower() == s.lower() for s in stringList)

#Returns 1 if string is contained in a string in stringList, otherwise 0.
#Note: boolean values False and True are considered to be 0 and 1, respectively,
#except when converted to string.
def containsStringCompare(string, stringList):
    return any(string.lower() in s.lower()  for s in stringList)




#Returns list project names ordered by matching degree.
#Only take skills into account, not languages, etc.
def compareSkills():
    output = {} #projectName -> degree of match
    sourceSkillList = [""]
    projectSkillDict = {} #projectName -> [skillsRequired]
    stringComparefunction = strictCompare

    #TODO Get list of source(user) skills
    #TODO Get list of lists og target(project) skills

    for projectName in projectSkillDict:
        d = matchListsOfStrings(sourceSkillList, projectSkillDict[projectName], 
                            stringComparefunction)
        output[projectName] = d

    #sortedProjectList = sorted(output.items(), key=operator.itemgetter(1))
    sortedProjectList = sorted(output, key=output.get)

    return sortedProjectList
    
