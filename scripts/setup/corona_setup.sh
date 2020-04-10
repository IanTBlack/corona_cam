#!/bin/bash

echo "Moving to home directory..."
cd /home/pi/
sleep 1s

echo "Beginning installation..."
sleep 1s

echo "Checking for updates..."
sudo apt-get -y update
sudo apt-get -y upgrade
sleep 1s

echo "Installing IDLE..."
sudo apt-get install idle
sleep 1s

echo "Installing modules..."
sudo pip3 install picamera
sudo pip3 install datetime
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sleep 1s

echo "Setting up directories..."
cd /home/pi/corona_cam/
mkdir h264

echo "Setting up scripts..."
cd /home/pi/corona_cam/scripts
chmod +x corona_boot.sh
chmod +x corona_cam.py
sleep 1s

echo "Checking for updates again..."
sudo apt-get -y update
sudo apt-get -y upgrade
sleep 1s


echo "Rebooting in 10 seconds..."
sleep 10s
sudo reboot