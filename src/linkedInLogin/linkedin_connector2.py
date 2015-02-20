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

# Only skills:
#fields = 'skills'
# Full extraction:
fields = "id," + "first-name," + "last-name," + "headline," + "picture-url," + "industry," + "summary," + "specialties," + "positions:(" + "id," + "title," + "summary," + "start-date," + "end-date," + "is-current," + "company:(" + "id," + "name," + "type," + "size," + "industry," + "ticker)" +")," + "educations:(" + "id," + "school-name," + "field-of-study," + "start-date," + "end-date," + "degree," + "activities," + "notes)," + "associations," + "interests," + "num-recommenders," + "date-of-birth," + "publications:(" + "id," + "title," + "publisher:(name)," + "authors:(id,name)," + "date," + "url," + "summary)," + "patents:(" + "id," + "title," + "summary," + "number," + "status:(id,name)," + "office:(name)," + "inventors:(id,name)," + "date," + "url)," + "languages:(" + "id," + "language:(name)," + "proficiency:(level,name))," + "skills:(" + "id," + "skill:(name))," + "certifications:(" + "id," + "name," + "authority:(name)," + "number," + "start-date," + "end-date)," + "courses:(" + "id," + "name," + "number)," + "recommendations-received:(" + "id," + "recommendation-type," + "recommendation-text," + "recommender)," + "honors-awards," + "three-current-positions," + "three-past-positions," + "volunteer"

print application.get_profile(None, None, fields)