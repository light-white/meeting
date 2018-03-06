#!/bin/bash
psid=`ps aux | grep "meeting_uwsgi" | grep -v "grep" | wc -l`
if [ ${psid} -gt 4 ]
then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
else
    echo "No uwsgi running!"
fi
