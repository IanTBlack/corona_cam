# Corona Cam
[The In-situ Plankton Assemblage eXplorer (IPAX) was developed by Pichaya Lertvilai at UCSD](https://agu.confex.com/agu/osm20/meetingapp.cgi/Paper/648464). The Corona Cam is and attempt at recreating the IPAX that was presented at Ocean Sciences Meeting 2020. The repo for the IPAX is located here [link once available].

The Corona Cam took approximately 8 pots of coffee and 72 Coronas to complete.

![Cam_Tall](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/full_tall.jpg)

![Cam_Face](https://github.com/IanTBlack/corona_cam/blob/master/documentation/images/full_face.jpg)

## Repository Structure
### 3d_prints
This folder contains .ipt, .stl, and .gcode files for the camera mount, battery mount, and camera setup tool. For the .gcode files, Ultimaker Cura 4.5 was used as the slicer for printing on an Ender 5 Pro. The readme.txt file in that folder details the settings used. All three parts require approximately 300g of PLA and ~21 hours of print time.

### documentation
This folder contains drawings, guides, and manuals that were used in the development of the Corona Cam. It is recommended that you review this material if you run into any issues.
A build list is also provided. The primary vendors in this build list are Adafruit, Amazon, Blue Robotics, DLS Corp, and M12 Lenses. Note that the total price listed in the build list only considers the primary parts and does not consider 3D printing costs, consumables, tools, or other peripheral electronics.

### scripts
This folder contains scripts for testing build components, a script that should be run at reboot, and the main operating script.

### setup
This folder contains a shell script that initially sets up the RPi with the necessary libraries and software. There is also an instructions.md file that provides step-by-step instructions for further setting up the camera from build to production.
Note that these instructions consider use of the Raspbian GUI while deployment considers use of the command line interface.


# Issues
If you have the zero2go software installed, and then install it again, it may cause comms issues with the pHat. For the time being, I've removed the zero2go portion of the corona_setup.sh script. This software will need to be installed manually before you hook up the pHat
