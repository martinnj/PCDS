# Python2.7

from linkedin import linkedin

API_KEY = '75yv7bexwfjovt' #Leapkit unique API/Consumer key
API_SECRET = 'Jz3ElgF0hj1RAjb3' #Leapkit unique Secret key/Consumer Secret


#RETURN_URL = 'http://localhost:8000'
RETURN_URL = 'http://www.google.com'

authentication = linkedin.LinkedInAuthentication(API_KEY, 
                                                 API_SECRET, 
                                                 RETURN_URL, 
                                                 linkedin.PERMISSIONS
                                                    .enums.values())

print 'Copy/paste the following URL to your browser:\n'
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)



