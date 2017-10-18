#!/bin/bash
python manage.py db migrate -m "add user profile"
python manage.py db migrate
