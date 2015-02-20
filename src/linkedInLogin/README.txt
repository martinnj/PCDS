Setup environment in terminal:
GOTO ../PCDS/src/linkedInLogin

Run command:
source env/bin/activate


You can now run code, e.g.

python linkedin_connector.py
python linkedin_connector2.py

linkedin_connector.py: Example of redirection to loginportal and after login and redirection to set url, here www.leapkit.com along with extracting all information about user.

linkedin_connector2.py: Example of data extraction directly from my acc, only for initial testing.


Note that only python2.7 works with the imported library python_linkedin.
The environment setup standard python to be python2.7.

Library python_linkedin: https://github.com/ozgur/python-linkedin