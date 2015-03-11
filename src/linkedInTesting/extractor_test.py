#!/usr/bin/env python
# Unit tests that checks that the LinkedIn extractor outputs expected json.

import json
from linkedin import linkedin

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class LinkedInExtractorTest(unittest.TestCase):
    #@unittest.skip("demonstrating skipping")
    #def test_skipped(self):
    #    self.fail("shouldn't happen")

    #def test_pass(self):
    #    self.assertEqual(10, 7 + 3)


    def test(self):
        # Setup for our test profile. We know the values in the profile and can
        # create a suitable test from them.
        CONSUMER_KEY = '77d39rnu0jgxhc'
        CONSUMER_SECRET = 'SRjbrl5ajSwkbpMH'
        USER_TOKEN = 'c87cfe99-0997-4393-bc8a-09bc60bbbaf4'
        USER_SECRET = '1e37a040-934a-4047-8852-4fdc5c378b7c'

        RETURN_URL = 'http://www.google.com'
        FILE_NAME = 'linkedInResult.json'

        authentication = linkedin.LinkedInDeveloperAuthentication(
                                            CONSUMER_KEY, 
                                            CONSUMER_SECRET, 
                                            USER_TOKEN, USER_SECRET, 
                                            RETURN_URL, 
                                            linkedin.PERMISSIONS.enums.values())
        application = linkedin.LinkedInApplication(authentication)

        #CHECK SKILLS
        fields = "first-name,last-name,skills"
        data = application.get_profile(None, None, fields)
        firstname = data['firstName']
        lastname = data['lastName']
        skills = data['skills']
        totalSkills = skills['_total']
        skillList = skills['values']
        neededSkills = ["PHP",
                        "Python",
                        "Management",
                        "Scrum",
                        "People Skills",
                        "Synergies",
                        "Love Of Learning",
                        "Bearings",
                        "Pipe",
                        "COBOL",
                        "Brain Tumors",
                        "Testing",
                        "Debugging",
                        "Entertainment",
                        "Enterprise Software"]

        self.assertEqual(firstname, "test")
        self.assertEqual(lastname, "profile")
        self.assertEqual(totalSkills, 15)
        for skill in skillList:
            skillstr = skill['skill']['name']
            if not(skillstr in neededSkills):
                self.fail("Unexpected skill:" + skillstr)
            else:
                neededSkills.remove(skillstr)
        self.assertEqual(len(neededSkills),0)
            


        #with open(FILE_NAME, 'w') as outfile:
        #    json.dump(skillList, outfile)