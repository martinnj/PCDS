Setup environment in terminal

INSTALL ENVIRONMENT
--Expects python2.7 and pip is installed.
--If Python's virtualenv is not installed; install it:
pip install virtualenv

--Goto folder of src files.
cd ../PCDS/src
--Create hidden environment and activate it
virtualenv -p /usr/bin/python2 .env
source .env/bin/activate
--Now install requirements:
pip install -r requirements.txt
-- You should now be able to run the code:

python main.py
python loginLinkedIn/linkedin_connector.py


main.py: 
    Opens browser to login to LinkedIn, extracts information and stores 
    this via Django in the local database file.

requirements.txt: 
    Contains required packages/libs to be installed in the 
    virtual environment.

loginLinkedIn: 
    Contains code for login and extraction of information from 
    LinkedIn. Saves in linkedInResult.json.
linkedInExtract: 
    Contains code for parsing and storing extracted information in a database
    via Django.