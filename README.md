# Corona Cam
[The original In-situ Plankton Assemblage eXplorer (IPAX) was developed by Pichaya Lertvilai at UCSD](https://agu.confex.com/agu/osm20/meetingapp.cgi/Paper/648464). The Corona Cam is an attempt at recreating the IPAX that was presented at Ocean Sciences Meeting 2020. Similar to the IPAX, the Corona Cam seeks to provide a low cost method (~400 USD) for in-situ photography and video recording of very tiny things in the ocean (50-200 microns), such as zooplankton.

**Specs**

Sensor Type: Sony IMX219 8MP

Lens: 1/2.5" 4mm M12 (swappable)

Case: Blue Robotics 3" Watertight Enclosure (rated for 100m depth)

Battery: 5V rechargeable lithium-ion (i.e. cell phone power pack)

Video Resolution, Framerate, Format: 1920x1080, 30, .h264

Still Image Resolution: 3280x2464  

![Face](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/full_tall.jpg)

![Side](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/side3.jpg)



The Corona Cam took approximately 9 pots of coffee and 72 Coronas to develop.



## Operation
The camera utilizes cron to operate the camera at user-defined times. This allows the camera to operate at intervals or at specific times. The length of the recording, the recording format, and LED colors and intensity are controlled by the Python script that is run through cron.



## Repository Structure
### 3d_prints
This folder contains .ipt, .stl, and .gcode files for the camera mount, battery mount, and camera setup tool. For the .gcode files, Ultimaker Cura 4.5 was used as the slicer for printing on an Ender 5 Pro. The readme.txt file in that folder details the settings used. All three parts require approximately 300g of PLA and ~21 hours of print time.

### documentation
This folder contains drawings, guides, and manuals that were used in the development of the Corona Cam. It is recommended that you review this material if you run into any issues.
A build list is also provided. The primary vendors in this build list are Adafruit, Amazon, Blue Robotics, DLS Corp, and M12 Lenses. Note that the total price listed in the build list only considers the primary parts and does not consider 3D printing costs, consumables, tools, or other peripheral electronics (monitor, keyboard, mouse).

### scripts
This folder contains scripts for testing build components, a script that assists with setting up the Pi, and scripts that are run under crontab.
