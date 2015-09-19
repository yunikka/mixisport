#!/bin/sh
#/usr/local/bin/gunicorn mixisport.wsgi:application --bind 127.0.0.1:3110 --workers 3 --pid /var/run/mixisport.pid --error-logfile /var/log/django/mixisport.log --daemon

/usr/local/bin/gunicorn mixisport.wsgi:application --bind 127.0.0.1:3102 --workers 3 --pid /var/run/mixisport_stage.pid --error-logfile /var/log/django/mixisport_stage.log --daemon
