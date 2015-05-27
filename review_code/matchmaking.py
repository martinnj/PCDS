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

    return float(matchSum) / len(sourceList)




#Returns 1 if string is equal to a string in stringList, otherwise 0.
def strictCompare(string, stringList):
    return any(string.lower() == s.lower() for s in stringList)

#Returns 1 if string is contained in a string in stringList, otherwise 0.
#Note: boolean values False and True are considered to be 0 and 1, respectively,
#except when converted to string.
def containsStringCompare(string, stringList):
    return any(string.lower() in s.lower() for s in stringList)

def skillsInDescription(skillList, full_description):
    return any(skill.lower() in full_description[0].lower() for skill in skillList)




#Returns list project names ordered by matching degree.
#Only take skills into account, not languages, etc.
def compareSkills(userSkills, projects, stringComparefunction=strictCompare):

    sortedProjectList = [(projId, matchListsOfStrings(userSkills, projSkills, stringComparefunction) ) for projId, projSkills in projects]
    sortedProjectList.sort(key=lambda tup: tup[1], reverse=True)

    return sortedProjectList