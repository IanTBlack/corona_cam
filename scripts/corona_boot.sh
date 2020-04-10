#!/bin/bash

sleep 600s  #Sleep for 600 seconds. 

sudo /usr/bin/tvservice -o  #Turn off the HDMI port.
sudo /opt/vc/bin/tvservice -o

echo none | sudo tee /sys/class/leds/led0/trigger  #Turn off the ACT LED.
echo 1 | sudo tee /sys/class/leds/led0/brightness

sudo iwconfig wlan0 txpower off  #Turn off the WiFi.
