# Instructions

## 1) Raspbian Install
I first recommend formatting your microSD card to FAT32. [The SD Association provides a simple application for formatting SD cards.](https://www.sdcard.org/downloads/formatter/)

There are a couple of ways you can flash Raspbian to your microSD card. The easiest method is to use [NOOBS](https://www.raspberrypi.org/downloads/noobs/), which walks you through setting up a Raspberry Pi through a graphical user interface (GUI). The second easiest method is to use the new [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/), which provides a graphical user interface (GUI) for flashing Raspbian to your SD card, but does not set up things for you once installed.

Another method is to download the [Raspbian zip file](https://www.raspberrypi.org/downloads/raspbian/), unzip it with [7-zip (Windows)](https://www.7-zip.org/download.html) or [The Unarchiver(Mac)](https://theunarchiver.com/), and then flash the Raspbian img to your microSD card with an [imager that works with your system](https://www.raspberrypi.org/documentation/installation/installing-images/).  

Note: These instructions consider the use of the Raspbian GUI to facilitate easier setup and so that video recordings can be previewed when tuning the camera. When deploying the camera, I recommend having the Pi boot to the command line interface (CLI), this frees up memory and slightly reduces power consumption.

## 2) GitHub Repository Download
Instead of having to download files individually, you can download the whole GitHub repository using the git clone command.
Open terminal and ensure that you are in the default directory by entering the command:

```bash
cd /home/pi
```

Next, enter the command:

```bash
git clone https://github.com/IanTBlack/corona_cam.git
```

This will initiate a download of the entire repository. It may take a few minutes to download.

## 3) Changing Interface Settings
After you download the corona_cam repository, but before you run the setup script, you need to change a few interface settings on the Pi.

The Corona Cam requires the use of the camera, I2C, and serial port interfaces. If you are running the NeoPixel without sudo, you'll also need to activate the SPI interface.
You can change these settings by going to Applications Menu (raspberr icon on taskbar) > Preferences > Raspberry Pi Configuration. Once the configuration window opens, go to the Interfaces tab and enable camera, I2C, Serial Port, and Serial Console. Once you enable these, the RPi will ask to reboot.

Alternatively, you can open a terminal and enter the command: 'sudo raspi-config'. This provides a text-based interface for configuring the RPi.

## 4) Setting up the PiRTC (DS3231)
After you have soldered the headers to the RPi Zero W, attach the PiRTC with coin cell installed. The directions outlined below are specific to the DS3231 PiRTC and also available in the [documentation/adafruit folder](https://github.com/IanTBlack/corona_cam/blob/master/documentation/adafruit/pi_rtc_adafruit_guide.pdf).

First, make sure the Pi is set to the timezone that you want. To make it simple, I usually set the timezone to UTC.

Next, open a terminal session and enter:
```bash
sudo i2cdetect -y 1
```

You should see the number 68. This is the address of the PiRTC.

Next, we need to edit the boot configuration file. Issue the command:
```bash
sudo nano /boot/config.txt
```
Using the down arrow on the keyboard, scroll to the bottom of the file.
Type the following on a new line (without the ''): 'dtoverlay=i2c-rtc,ds3231'
On the line below that one, type (without the ''): 'disable_camera_led=1'
Type CTRL + O to write the changes. Then CTRL + X to exit the editor.
The first line we added above identifies the RTC as the DS3231.
The second line we added makes sure that the camera LED stays off.


To confirm your changes, type
```bash
sudo less /boot/config.txt
```

If everything looks good, restart the Pi with:

```bash
sudo reboot
```

Once the RPi is back up, we'll need to turn off the fake clock and tell the Pi to read from the PiRTC.

Issue the following:
```bash
sudo apt-get -y remove fake-hwclock
sudo update-rc.d -f fake-hwclock remove
sudo systemctl disable fake-hwclock
```

Once those commands have run their course, we'll need to edit another script.
Run:
```bash
sudo nano /lib/udev/hwclock-set
```
This will open a file for the original "hardware clock".
In this file, comment out the following lines with a '#' at the beginning of the line so that they look like this.

```bash
#if[-e /run/systemd/system]; then
# exit 0'
#fi
```

Scroll a little further down the file and also comment out these lines:

```bash
#/sbin/hwclock --rtc=$dev --systz --badyear
#/sbin/hwclock ==rtc=$dev --systz
```
Write out the script editor with CTRL + O and then exit with CTRL + X.

Next, check the clock time with
```bash
sudo hwclock -D -r
```
It should be wrong because we haven't set the time yet. Issue the following command to confirm that the time that be Pi states is correct.

```bash
date
```

To write the Pi time to the PiRTC, issue the command:
```bash
sudo hwclock -w
```

Then to check the PiRTC time:
```bash
sudo hwclock -r
```

The clock should now report the correct time.


## 5) Protoboard Setup and Testing
Next you can solder the tall headers and the terminal block to the protoboard.
We are using tall headers here because this allows the protoboard to stack on top of the Pi, and then the PiRTC on top of the protoboard.

![Headers](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/proto_head_block.jpg)
![Wires](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/proto_wires.jpg)

In my version, I set up wires running from 5V, GND, Pin 21, and MOSI to pins on the terminal block. During testing, having the NeoPixel hooked up to MOSI allows you to not run the script as sudo, but can sometimes cause flickering. When deploying the camera, I have the NeoPixel hooked up the Pin 21.

## 6) NeoPixel Setup
Solder wires (~12cm long) to the V+, GND, and Input on the NeoPixel ring. Take care when doing this, as too much solder can short the ring, causing only some of the LEDs to light up.

## 7) Camera Side Setup
Install the 3D printed camera mount into the 3" Blue Robotics Flange using 10mm long, 3mm hex bolts. Then install 8mm M2.5 standoffs for the camera and 6mm M2.5 standoffs for the Pi.
![Mount](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/print_cam_w_standoffs.jpg)

Attach the camera cable to the camera. Install the camera into the 3D print. Use M2.5 nuts to secure the camera.
![Cam_Install](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/cam_install.jpg)

Next, thread the NeoPixel wires through the slots.

![NeoPixel Wires](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/neopixel_wires.jpg)

Attach the camera cable to the Pi, and then install the Pi onto the 3D print. Secure the Pi in place with 12mm M2.5 standoffs.

![Pi_Standoffs](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/pi_install.jpg)

Install the protoboard setup on top of the Pi. Use 12mm M2.5 standoff to secure it in place.

![Proto_Standoffs](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/proto_no_wires.jpg)

Attach the Pi on top of the protoboard and secure with a M2.5 nut. Connect the NeoPixel wires to the appropriate terminal block locations.

![RTC_Wires](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/pi_wires_rtc.jpg)
![Side](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/side.jpg)
![Back](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/back_headers.jpg)
![Build](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/camera_build.jpg)

## 8) Battery Side Setup
Install the Blue Robotics vent, switch, and blank plugs into the 4-hole end cap. Ensure that the o-rings are clean and greased.

Attach the 3D printed battery mount to the flange with two 10mm long M3 bolts. The switch should be oriented so that it is above the battery tray.

To make the switch cable, I found a microUSB cable that had enough clearance when plugged into the USB port on the PiZeroW. The PiZeroW USB port can also act as a power port for 5V sources. I took my cable and cut it in half. I then resoldered the GND sides back together, and for each V+ side, I soldered the switch wires that Blue Robotics provided with the switch. I would recommend purchasing a microUSB cable that has a 90 degree bend.

![Battery Side](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/battery_tray.jpg)


## 9) Testing
After you have set up the NeoPixel, RTC, and camera you can test the build while it is attached to a monitor, keyboard, and mouse.
In terminal:
```bash
sudo python3 /home/pi/corona_cam/scripts/corona_cam.py
```

You should see that the LEDs turn blue for 30 seconds, then they turn white for 60 seconds. No preview should appear on the monitor (because it is currently disabled in the  Python script). To activate the preview in the corona_cam.py script, you will need to uncomment all lines that pertain to the camera preview in the run_camera function.

You can confirm that the camera produced a video by navigating to the h264 folder.

To test the camera, you can issue the command:

```bash
raspistill -t 60000
```
This will turn on the camera for 60 seconds and will display a preview on the monitor.
Utilizing this raspistill command is useful when tuning the camera. Setting up the 3D printed setup tool while the acrylic end cap is installed provides 4cm distance between the camera lens and the setup tool face. This provides about a 2cm viewing area.

Once you are satisfied that the camera is operating correctly, you can set up a cron to run the corona_boot.sh script and the corona_cam.py script.

## 10) Crontab Setup
There are two scripts that need to be set up in Crontab in order for the camera to work. The corona_at_boot.sh script is a shell script that waits for 300s (5 minutes) after the Pi boots up before it turns off the HDMI port, WiFi, and ACT LED. During this five minutes, if you want to access the Pi, you can plug into it, comment out the boot script in Crontab and reboot the RPi..

The second script is the main operating code for the camera. You can set the frequency that the camera records. This can be done as an interval (i.e. every 60 minutes), or you can set it up to record at a specific time (i.e every hour at two minutes past the hour). Remember, this just modifies how often the camera records. If you want to change the length of time that the camera records, you'll need to change the record_time value in the Python script.

If this is your first time setting up crontab, the easiest method is to use nano (method #1). At the bottom of the file, enter the following line:

```bash
 @reboot sudo sh /home/pi/corona_cam/scripts/corona_at_boot.sh
```

If you want to run the script every 15 minutes (independent of the clock time), enter the following:

```bash
*/15 * * * * sudo python3 /home/pi/corona_cam/scripts/corona_cam.py
```

If you want to run the script 15 minutes past the hour every hour, enter the following
```bash
15 * * * * sudo python3 /home/pi/corona_cam/scripts/corona_cam.py
````

This becomes particularly handy if you modify the corona_cam script and make copies that operate for different time lengths, take pictures, have different camera resolutions, different LED colors, etc. You could have two different scripts run at different times.

[Crontab Guru](https://crontab.guru/#*_*_*_*_*) is a handy tool for determining crontab scheduling.


## 11) Final Seal
Things to consider before deployment.
- Is the battery charged and zip-tied in place?
- Do any of the acrylic pieces have scratches that would cause flooding?
- Are all of the o-rings in place and greased (especially the end caps, vent, and switch)?
- Did I add a desiccant pack?
- Is there enough space on the SD card?
- Did I set up the crontab correctly?
- Did I apply a vacuum to the unit?
