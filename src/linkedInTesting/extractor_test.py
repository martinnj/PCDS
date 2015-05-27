#!/usr/bin/env python
# Unit tests that checks that the LinkedIn extractor outputs expected json.

import json
from linkedin import linkedin

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class LinkedInExtractorTest(unittest.TestCase):
    """
    Unit test suite that tests the LinkedIn Extraction library.
    """


    def test(self):
        """
        Main test method for testing the extractors.
        """

        # Constants needed to test the extractor.
        # NOTE: The test is using a fake LinkedIn profile we created.
        # This means we know what names/skills should be returned and how many.

        # API keys
        CONSUMER_KEY = '77d39rnu0jgxhc'
        CONSUMER_SECRET = 'SRjbrl5ajSwkbpMH'
        USER_TOKEN = 'c87cfe99-0997-4393-bc8a-09bc60bbbaf4'
        USER_SECRET = '1e37a040-934a-4047-8852-4fdc5c378b7c'
        RETURN_URL = 'http://www.google.com'
        # Skills we have entered for the profile.
        NEEDEDSKILLS = ["PHP",
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

        # Authenticate and create an application.
        authentication = linkedin.LinkedInDeveloperAuthentication(
                                            CONSUMER_KEY, 
                                            CONSUMER_SECRET, 
                                            USER_TOKEN, USER_SECRET, 
                                            RETURN_URL, 
                                            linkedin.PERMISSIONS.enums.values())
        application = linkedin.LinkedInApplication(authentication)

        # Extract the following fields from the profile.
        fields = "first-name,last-name,skills"
        data = application.get_profile(None, None, fields)

        # Get the fields we need from the JSON.
        firstname = data['firstName']
        lastname = data['lastName']
        skills = data['skills']
        totalSkills = skills['_total']
        skillList = skills['values']

        # Check of the names are correct and  that
        # the correct number of skills was returned.
        self.assertEqual(firstname, "test")
        self.assertEqual(lastname, "profile")
        self.assertEqual(totalSkills, 15)

        # Loop through the skills and check that they are what we expect.
        for skill in skillList:
            skillstr = skill['skill']['name']
            if not(skillstr in NEEDEDSKILLS):
                self.fail("Unexpected skill:" + skillstr)
            else:
                NEEDEDSKILLS.remove(skillstr)

        # Check that we did recieve all the expected skills.
        self.assertEqual(len(NEEDEDSKILLS),0)
