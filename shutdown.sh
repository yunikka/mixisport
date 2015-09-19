#!/bin/sh

#kill -9 `cat "/var/run/mixisport.pid"` >/dev/null 2>&1
kill -9 `cat "/var/run/mixisport_stage.pid"` >/dev/null 2>&1
rm /var/run/mixisport_stage.pid
