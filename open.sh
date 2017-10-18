#!/bin/bash
./exp.sh
python sunny.py --clientid=1ffda6947c3b9e2d
python ./manage.py runserver --host 0.0.0.0
