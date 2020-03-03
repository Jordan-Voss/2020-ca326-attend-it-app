#!/bin/sh
sudo iw wlan0 station dump >> /home/pi/Desktop/mac.txt
python3 /home/pi/Desktop/rasp.py