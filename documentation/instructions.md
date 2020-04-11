# Instructions

## 1) Raspbian Install
I first recommend formatting your microSD card to FAT32. [The SD Association provides a simple application for formatting SD cards.](https://www.sdcard.org/downloads/formatter/)

There are a couple of ways you can flash Raspbian to your microSD card. The easiest method is to use [NOOBS](https://www.raspberrypi.org/downloads/noobs/), which walks you through setting up a Raspberry Pi through a graphical user interface (GUI). The second easiest method is to use the new [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/), which provides a graphical user interface (GUI) for flashing Raspbian to your SD card, but does not set up things for you once installed.

Another method is to download the [Raspbian zip file](https://www.raspberrypi.org/downloads/raspbian/), unzip it with [7-zip (Windows)](https://www.7-zip.org/download.html) or [The Unarchiver(Mac)](https://theunarchiver.com/), and then flash the Raspbian img to your microSD card with an [imager that works with your system](https://www.raspberrypi.org/documentation/installation/installing-images/).  

Note: These instructions consider the use of the Raspbian GUI to facilitate easier setup and so that video recordings can be previewed when tuning the camera. When deploying the camera, I recommend having the Pi boot to the command line interface (CLI), this frees up memory and slightly reduces power consumption.

## 2) GitHub Repository Download
Instead of having to download files individually, you can download the whole GitHub repository using the git clone command.
Open terminal and ensure that you are in the default directory (/home/pi).

Next, enter the command:

```shell
git clone https://github.com/IanTBlack/corona_cam.git
```

```bash
git clone https://github.com/IanTBlack/corona_cam.git
```

This will initiate a download of the entire repository.

## 3) Changing Interface Settings
The Corona Cam requires the use of the camera, I2C, and serial port interfaces. If you are running the NeoPixel without sudo, you'll also need to activate the SPI interface.
You can change this settings by going to Applications Menu (Raspberry Icon) > Preferences > Raspberry Pi Configuration. Once the configuration window opens, go to the Interfaces tab and enable camera, I2C, Serial Port, and Serial Console. Once you enable these, the RPi will ask to reboot.

Alternatively, you can open a terminal and enter the command: 'sudo raspi-config'. This provides a text-based interface for configuring the RPi.

## 4) Setting up the PiRTC (DS3231)
After you have soldered the headers to the RPi Zero W, attach the PiRTC with coin cell installed. The directions outlined below are specific to the DS3231 PiRTC and also available in the documentation/adafruit folder.

First, make sure the Pi is set to the timezone that you want. To make it simple, I usually set the timezone to UTC.


In terminal:

'sudo i2cdetect -y 1'

You should see the number 68. This is the address of the PiRTC.

Next, issue: 'sudo nano /boot/config.txt'
Using the down arrow on the keyboard, scroll to the bottom of the file.

Type the following on a new line: 'dtoverlay=i2c-rtc,ds3231'
On the next new line, type: 'disable_camera_led=1'
Type CTRL-O to write the changes. Then CTRL-X to exit the editor.
To confirm your changes, type sudo less /boot/config.txt and scroll to the bottom.
Restart the RPi with sudo reboot.

Once the RPi is back up, we'll need to turn off the fake clock and tell the Pi to read from the PiRTC.

Issue the following:
'sudo apt-get -y remove fake-hwclock'
'sudo update-rc.d -f fake-hwclock remove'
'sudo systemctl disable fake-hwclock'

Once those commands have run their course, we'll need to edit another script.

Run: 'sudo nano /lib/udev/hwclock-set'
This will open a file for the original "hardware clock".
In this file, comment out the following lines with a '#' at the beginning of the line so that they look like this.

'#if[-e /run/systemd/system]; then'
'# exit 0'
'#fi'

Scroll a little further down the file and also comment out these lines:

'/sbin/hwclock --rtc=$dev --systz --badyear'
'/sbin/hwclock ==rtc=$dev --systz'

Write out the script editor with CTRL + O and then exit with CTRL + X.

Next, check the clock time with 'sudo hwclock -D -r'. It should be wrong because we haven't set the time yet.

Issue the 'date' command. Verify that the time is correct.
Issue 'sudo hwclock -w'. This writes the time to the PiRTC.
Issue another 'sudo hwclock -r' to check the time on the Pi.

The clock should now report the correct time.

## 5) Protoboard Setup and Testing
Next you can solder the tall headers and the terminal block to the protoboard.
We are using tall headers here because this allows the protoboard to stack on top of the Pi, and then the PiRTC on top of the protoboard.

Figure here

In my version, I set up wires running from V+, GND, Pin 21, and MOSI to pins on the terminal block. During testing having the NeoPixel hooked up to MOSI allows you to not run the script as sudo, but can sometimes cause flickering. When deploying the camera, I have the NeoPixel hooked up the Pin 21.

## 6) NeoPixel Setup
Solder wires (~12cm long) to the V+, GND, and Input on the NeoPixel ring. Take care when doing this, as too much solder can short the ring, causing only some of the LEDs to light up.

## 7) Testing



## Crontab Setup
There are two scripts that need to be set up in Crontab in order for the camera to work. The corona_at_boot.sh script is a shell script that waits for 300s (5 minutes) after the Pi boots up before it turns off the HDMI port, WiFi, and ACT LED. During this five minutes, if you want to access the Pi, you can plug into it, comment out the boot script in Crontab and reboot the RPi..

The second script is the main operating code for the camera. You can set the frequency that the camera records. This can be done as an interval (i.e. every 60 minutes), or you can set it up to record at a specific time (i.e every hour at two minutes past the hour). Remember, this just modifies how often the camera records. If you want to change the length of time that the camera records, you'll need to change the record_time value in the Python script.

If this is your first time setting up crontab, the easiest method is to use nano (method #1). At the bottom of the file, enter the following line:

> @reboot sudo sh /home/pi/corona_cam/scripts/corona_at_boot.sh


If you want to run the script every 15 minutes (independent of the clock time), enter the following:

> */15 * * * * sudo python3 /home/pi/corona_cam/scripts/corona_cam.py

If you want to run the script 15 minutes past the hour every hour, enter the following
15 * * * * sudo python3 /home/pi/corona_cam/scripts/corona_cam.py

This becomes particularly handy if you modify the corona_cam script and make copies that operate for different time lengths, take pictures, have different camera resolutions, different LED colors, etc. You could have two different scripts run at different times.


[Crontab Guru](https://crontab.guru/#*_*_*_*_*) is a handy tool for determining crontab scheduling.

## Switch Cable
For this version, I found a microUSB cable that had enough clearance when plugged into the USB port on the PiZeroW. The PiZeroW USB port can also act as a power port for 5V sources. I took my cable and cut it in half. I resoldered the GND sides back together, and for each V+ side, I soldered the switch wires that Blue Robotics provided with the switch.

I would recommend purchasing a microUSB cable that has a 90 degree bend.
