#!/bin/bash
<<<<<<< HEAD
echo Create/overwrite hidden environment and activate it
virtualenv -p /usr/bin/python2 .env
source .env/bin/activate
echo Successfully installed environment
=======
#echo Create hidden environment
#virtualenv -p /usr/bin/python2.7 .env

#echo Activate virtual environment
#source .env/bin/activate
#echo Successfully installed environment

>>>>>>> ba8cb7affbf78e0deed980de02a1cf6e0228c1a4
echo Now installing requirements
pip install -r requirements.txt
echo Successfully installed requirements.

echo Run python unittests.
echo Running py.test
py.test
#local RES=$(py.test)
#rm -rf .env
#return $RES
