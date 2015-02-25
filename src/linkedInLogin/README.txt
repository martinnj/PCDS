Setup environment in terminal:
GOTO ../PCDS/src/linkedInLogin

INSTALL ENVIRONMENT
--Excepts python2.7 and pip is installed.
--If Python's virtualenv is not installed; install it:
pip install virtualenv

--Goto folder of src files.
cd ../PCDS/src/linkedInLogin
--Create hidden environment and activate it
virtualenv -p /usr/bin/python2 .env
source .env/bin/activate
--Now install requirements:
pip install -r requirements.txt
-- You should now be able to run the code:


You can now run code, e.g.

python linkedin_connector.py
python linkedin_connector2.py

linkedin_connector.py: Example of redirection to loginportal and after login and redirection to set url, here www.leapkit.com along with extracting all information about user.

linkedin_connector2.py: Example of data extraction directly from my acc, only for initial testing.


Note that only python2.7 works with the imported library python_linkedin.
The environment setup standard python to be python2.7.

Library python_linkedin: https://github.com/ozgur/python-linkedin