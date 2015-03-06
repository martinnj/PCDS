#!/bin/bash
echo Create hidden environment
virtualenv -p /usr/bin/python2 .env
echo Activate virtual environment
source .env/bin/activate
echo Successfully installed environment
echo Now installing requirements
pip install -r requirements.txt
echo Successfully installed requirements.
echo Run python unittests.
echo Running py.test
py.test
local RES=$(py.test)
rm -rf .env
return $RES