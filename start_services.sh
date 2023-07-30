#!/bin/bash

cd /home/raspberry/Desktop/Coffee_Proyect
ps -faux | grep -E "listener.py|server.py" | grep -v grep | awk '{print $2}' | while read line; do kill $line; done
python3 listener.py &
python3 server.py &
