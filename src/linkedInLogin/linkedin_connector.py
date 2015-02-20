# Python2.7

from linkedin import linkedin
from selenium.common.exceptions import TimeoutException
from httplib import CannotSendRequest


import contextlib
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import urlparse
import json

# Setup LinkedIn connection
API_KEY = '75yv7bexwfjovt' #Leapkit unique API/Consumer key
API_SECRET = 'Jz3ElgF0hj1RAjb3' #Leapkit unique Secret key/Consumer Secret

RETURN_URL = 'http://www.leapkit.com'
FILE_NAME = 'linkedInResult.json'

# Only extract skills:
#fields = 'skills'
# Full extraction:
fields = ("id," + "first-name," + "last-name," + "headline," + "picture-url," + 
          "industry," + "summary," + "specialties," + "positions:(" + "id," + 
          "title," + "summary," + "start-date," + "end-date," + "is-current," + 
          "company:(" + "id," + "name," + "type," + "size," + "industry," + 
          "ticker)" +")," + "educations:(" + "id," + "school-name," + 
          "field-of-study," + "start-date," + "end-date," + "degree," + 
          "activities," + "notes)," + "associations," + "interests," + 
          "num-recommenders," + "date-of-birth," + "publications:(" + "id," + 
          "title," + "publisher:(name)," + "authors:(id,name)," + "date," + 
          "url," + "summary)," + "patents:(" + "id," + "title," + "summary," + 
          "number," + "status:(id,name)," + "office:(name)," + 
          "inventors:(id,name)," + "date," + "url)," + "languages:(" + "id," + 
          "language:(name)," + "proficiency:(level,name))," + "skills:(" + 
          "id," + "skill:(name))," + "certifications:(" + "id," + "name," + 
          "authority:(name)," + "number," + "start-date," + "end-date)," + 
          "courses:(" + "id," + "name," + "number)," + 
          "recommendations-received:(" + "id," + "recommendation-type," + 
          "recommendation-text," + "recommender)," + "honors-awards," + 
          "three-current-positions," + "three-past-positions," + "volunteer")

timeout_seconds = 60 #secs before timeout when loggin in to LinkedIn.

authentication = linkedin.LinkedInAuthentication(API_KEY, 
                                                 API_SECRET, 
                                                 RETURN_URL, 
                                                 linkedin.PERMISSIONS
                                                    .enums.values())

#print authentication.authorization_url  # open this url on your browser

# Open browser with LinkedIN login. Then redirect to RETURN_URL
try:
    with contextlib.closing(webdriver.Firefox()) as driver:
        driver.get(authentication.authorization_url) #go to linkedin login site
        wait = ui.WebDriverWait(driver, timeout_seconds) # timeout after timeout_seconds
        #inputElement = driver.find_element_by_name('Leapkit') #'viewport')
        test = wait.until(lambda driver: driver.title == 'Leapkit') #Wait until leapkit homepage is loaded (redirected after login) or up to wait seconds.
except TimeoutException:
    print "Login took too much time!"
except CannotSendRequest:
    print "Cannot send request!"

# Get authorization_code from redirection uri and acquire access to LinkedIn information

redirect_uri = driver.current_url #Save the uri; contains authorization_code as param
query = urlparse.urlparse(redirect_uri).query #Parse uri
url_dict = urlparse.parse_qs(query)
authentication_code = url_dict['code'] #Get code

authentication.authorization_code = authentication_code #Set auth_code, lib does not do this smartly..

authentication.get_access_token() #Needed to access linkedin account info.
application = linkedin.LinkedInApplication(authentication) #Now get access


# Extract user information
data = application.get_profile(None, None, fields)
try:
    with open(FILE_NAME, 'w') as outfile:
        json.dump(data, outfile)
except IOError:
    print 'Cannot open or write to', FILE_NAME

print "Profile dumped to file: " + FILE_NAME


