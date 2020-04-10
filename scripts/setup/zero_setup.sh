#!/bin/bash

echo "Installing Zero2Go Omini software..."
cd /home/pi
wget http://www.uugear.com/repo/Zero2GoOmini/installZero2Go.sh
sudo sh installZero2Go.sh
echo "Zero2Go Omini software has been installed."

echo "Shutting down in 10 seconds..."
echo "After shutdown, you can install the Zero2Go Omini and power up the Pi again."
sleep 10s
sudo shutdown -h now