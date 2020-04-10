# Order of Operations
## Raspbian Install
I first recommend formatting your microSD card to FAT32.
[The SD Association provides a simple application for formatting SD cards.](https://www.sdcard.org/downloads/formatter/)

While your microSD card is formatting, you can download the [Raspbian Imager](https://www.raspberrypi.org/documentation/installation/installing-images/README.md), which allows you to flash Raspbian to the card. It is not recommended that you install Raspbian with NOOBS. If you decided to implement the Zero2Go Omini, NOOBS can cause problems with its operation.

Once your card has Raspbian loaded onto it, pop it into the RPiZeroW and fire up the system..

## GitHub Repository Download
Instead of having to download files individually, you can download the whole GitHub repository using the git clone command.
Open terminal and ensure that you are in the default directory (/home/pi).

Next, enter the command:

> git clone https://github.com/IanTBlack/corona_cam.git

This will initiate a download of the entire repository.

## Run Setup Script
I've created a shell script that will install the necessary python libraries and third party software for operating the camera. T
In terminal, execute the following commands:

> cd /home/pi/Corona_Cam/Setup
> chmod +x corona_setup.sh
> cd /home/pi/
> sudo sh /home/pi/corona_cam/setup/corona_setup.sh

This will install some libraries and setup a new directory in the corona_cam folder for recorded videos.

## Zero2Go Omini Setup and Testing

## Protoboard Setup and Testing

## RTC Setup and Testing

## Boot Script Setup

## Operating Script Setup


## Crontab Setup
There are two scripts that need to be set up in Crontab in order for the camera to work. The corona_at_boot.sh script is a shell script that waits for 600s (10 minutes) after the Pi boots up before it turns off the HDMI port, WiFi, and ACT LED. During this ten minutes, if you want to access the Pi, you can plug into it, comment out the boot script in Crontab, and the reboot it.

The second script is the main operating code for the camera. You can set the frequency that the camera records. This can be done as an interval (i.e. every 60 minutes), or you can set it up to record at a specific time (i.e every hour at two minutes past the hour). Remember, this just modifies how often the camera records. If you want to change the length of time that the camera records, you'll need to change the record_time value in the Python script.

If you kept the defaults, here is how you would set up the boot script via terminal.

> cd /corona_cam/scripts
> chmod +x corona_at_boot.sh
> cd /home/pi
> crontab -e

If this is your first time setting up crontab, the easiest method is to use method 1 (nano). At the bottom of the file, enter the following line:

> @reboot /home/pi/corona_cam/scripts/corona_at_boot.sh

Next, you'll want to add the operating script.

> cd /home/pi/corona_cam/scripts
> chmod +x corona_cam.py
> cd /home/pi
> crontab -e

If you want to run the script every 60 minutes (independent of the clock time), enter the following:

> */60 * * * * sudo python3 /home/pi/corona_cam/scripts/corona_cam.py

If you want to run the script 5 minutes past the hour every hour, enter the following
5 * * * * sudo python3 /home/pi/corona_cam/scripts/corona_cam.py


[Crontab Guru](https://crontab.guru/#*_*_*_*_*) is a handy tool for determining crontab scheduling.


Following these instructions in order is recommended.

1) Install SD Formatter  and format your SD card.

1) Flash Raspbian to your SD card. The easiest method is with the Raspbian Imager (https://www.raspberrypi.org/documentation/installation/installing-images/README.md)
   DO NOT INSTALL WITH NOOBS. Installing with NOOBS can cause problems with the Zero2Go Omini.


1) Run corona_setup.sh
	a) cd Corona_Cam
	b) chmod +x corona_setup.sh
	c) ./corona_setup.sh
	d) Once complete, the Pi will reboot.
