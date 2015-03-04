#!/bin/bash
echo Create hidden environment and activate it
virtualenv -p /usr/bin/python2 .env
source .env/bin/activate
echo Successfully installed environment
echo Now installing requirements
pip install -r requirements.txt
echo Successfully installed requirements.
echo Run python unittests.
echo Running py.test
local RES=$(py.test)
rm -rf .env
return $RES
