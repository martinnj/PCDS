from linkedInExtract.linkToLeap import fromFile
from linkedInExtract.linkToLeap import fromString
from linkedInTesting.linkedInJsonGenerator import generateAll 
import sys

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class LinkedInExtractorTest(unittest.TestCase):

    def compare(self, dic, json):
        structure = None
        structure = fromString(json) 
        # print structure
        # print dic
        for skill in structure.skills:
            found = dic["skills"]["values"] != [] #False
            # print found
            for value in dic["skills"]["values"]:
                # print skill.id +" == "+str(value["id"])
                found = found or (int(skill.id) == value["id"])
            # if not found:
                # print skill.name
                # print dic["skills"]["values"]
                # print dic
                # print json
            self.assertTrue(found)
        for language in structure.languages:
            found = dic["skills"]["values"] != [] #False
            # found = False
            for value in dic["languages"]["values"]:
                found = found or (int(language.id) == value["id"])
            # if not found:
                # print language.name
            self.assertTrue(found)
        self.assertEqual(dic["firstName"], structure.firstName)
        self.assertEqual(dic["maidenName"], structure.maidenName)
        self.assertEqual(dic["lastName"], structure.lastName)

    def test(self):
        (dics, filePathExtractedResults) = generateAll()
        with open(filePathExtractedResults) as f:
            lines = f.readlines()
        for i in range(len(lines)):
            self.compare(dics[i], lines[i])
