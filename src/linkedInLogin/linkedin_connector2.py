# Python2.7

from linkedin import linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application
CONSUMER_KEY = '75yv7bexwfjovt'
CONSUMER_SECRET = 'Jz3ElgF0hj1RAjb3'
USER_TOKEN = 'a0c8853f-d5aa-4dbb-98eb-7e5ad3c3d33f'
USER_SECRET = '84b2fe57-45fb-4cb7-a3d1-b564d7c3d131'

RETURN_URL = 'http://www.google.com'

# Instantiate the developer authentication class

authentication = linkedin.LinkedInDeveloperAuthentication(
                                            CONSUMER_KEY, 
                                            CONSUMER_SECRET, 
                                            USER_TOKEN, USER_SECRET, 
                                            RETURN_URL, 
                                            linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

print application.get_profile() 