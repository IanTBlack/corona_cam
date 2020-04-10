#!/bin/bash

echo "Installing Zero2Go Omini software..."
wget http://www.uugear.com/repo/Zero2GoOmini/installZero2Go.sh
sudo sh installZero2Go.sh
echo "Zero2Go Omini software has been installed."

echo "Rebooting in 10 seconds..."
sleep 10s
sudo reboot