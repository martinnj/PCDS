Notes from software review
==========================

Models.py
---------
- Be consistent about naming, keep to the Python standard or do camel case.


Matchmaking.py
--------------
- Good with keeping the compare fun generic and not domain specific.
- Matchmaking algorithm normalization will ignore number of mismatches, punishing people who have too many skills.
- Comments are not in python docstring type.


linkedin_converter.py/linkedin_connector.py
---------------------
- Looooooong lines are looooooong (Python max is 79).
- What fields to extract could be kept in the config file.