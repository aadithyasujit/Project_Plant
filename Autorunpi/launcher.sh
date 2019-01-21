#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Project_Plant/codes
sudo python3 Data_log.py
cd /
