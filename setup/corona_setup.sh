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

echo "Installing Zero2Go Omini software..."
wget http://www.uugear.com/repo/Zero2GoOmini/installZero2Go.sh
sudo sh installZero2Go.sh
echo "Zero2Go Omini software has been installed."

echo "Setting up directories..."
cd /home/pi/corona_cam/
mkdir h264

echo "Checking for updates again..."
sudo apt-get -y update
sudo apt-get -y upgrade
sleep 1s


echo "Rebooting in 30 seconds..."
sleep 10s
sudo reboot