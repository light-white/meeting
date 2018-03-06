#!/bin/bash
psid=`ps aux | grep "meeting_uwsgi" | grep -v "grep" | wc -l`
if [ ${psid} -gt 4 ]
then
    echo "uwsgi is running!"
else
    uwsgi /home/django/meeting/meeting_uwsgi.ini
    echo "Start uwsgi service [OK]"
fi
