#!/bin/bash
rm -rf ~/Documents/flasky/migrations
rm -f ~/Documents/flasky/data-dev.sqlite
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
