'''
The original In-situ Plankton Assemblage eXplorer (IPAX) was developed by Pichaya Lertvilai at UCSD.
This version utilizes a Sony IMX219 camera with a 4mm M12 lens and a Neopixel 16 LED ring.
This script will run the NeoPixel LEDs blue for 30 seconds, then turn the LEDs white and set the camera to record for 60 seconds at 1080p. 

Adjusting colors can be done through the neopixel color function.
Adjusting the recording length can be done in the run_camera function.

Author: iblack
Updated: 2020-04-09
Tested in Python 3.7.3 on Raspbian Buster on a Pi Zero.
'''


import os, time, datetime, picamera, board, neopixel 

def main():
    pixels = neopixel_setup(brightness = 1)  #Set up the neopixel object.
    neopixel_color(pixels,color = 'blank')  #Blank the LEDs.
    neopixel_color(pixels,color = 'blue')  #Turn on the LEDs to blue.
    time.sleep(30)  #Wait for 30 seconds (with the LEDs blue).
    run_camera(60,pixels)  #Record for 60s. Bring in the pixels object to control the LEDs. 
    neopixel_color(pixels,color = 'blank')  #Blank the LEDs.
    #os._exit(00)  #Reset the console so that the NeoPixel line clears in the event of failure. Needed if MOSI line is input for NeoPixel.
    return


def run_camera(record_time,pixels):
    os.chdir('/home/pi/corona_cam/h264')
    filename = set_filename(prefix = 'corona_cam',filetype = '.h264')  #The name issued here prepends the date and time in the returned filename.
    with picamera.PiCamera() as camera:
        #camera.rotation = 180  #Comment out or delete this line in deployment scenarios.
        #camera.preview_fullscreen = False
        #camera.preview_window = (1200,0,640,480)  #Format: Xpos, Ypos, Height, Width
        camera.led = False #Turn off the camera LED.
        camera.resolution = (1920,1080)  #Set resolution width and height.
        camera.framerate = 24  #Set the camera framerate.
        camera.annotate_background = picamera.Color('black')  #Make the timestamp background black so it is easier to see.
        camera.annotate_text_size = 16  #Set the timestamp font size.
        #camera.start_preview() #Initiate the preview. Used for testing.        
        camera.start_recording(filename)  #Name the output file based on the deployment site and datetime.   

        start = datetime.datetime.now()  #Establish the start time of the video.
        while (datetime.datetime.now() - start).seconds < record_time:  #Perform math to get difference in time between the start time and the "now" time.
            camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  #Annotate the video with the current time.
            camera.wait_recording(0)  #If an error occurs, this should catch it.     
            if (datetime.datetime.now() - start).seconds <= record_time and (datetime.datetime.now() - start).seconds > 0: #Turn the lights to white for a duration (seconds) equivalent to record_time.
                neopixel_color(pixels,color = 'white')  
            #else:
                #neopixel_color(pixels,color = 'blank')        #Turn off the LEDs if the value is not between 0 and record_time.
        neopixel_color(pixels,color = 'blank')        #Turn off the LEDs.
        #time.sleep(3)  #Record for an additional 3 seconds.
        #camera.stop_preview()  
        camera.stop_recording()        
        camera.close()  #Close out the camera.
    return


#Function that bulds the filename for the recording.
def set_filename(prefix = 'corona_cam',filetype = '.h264'):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M") #Add a timestamp to the filename in the format of YYYY-MM-DD_HHMM  
    filename = prefix + '_' + timestamp + filetype 
    return filename

#Function that sets up the neopixel object. 
def neopixel_setup(brightness = 1):
    pixel_pin = board.D21  #Define the data input pin for the Pi.
    num_pixels = 16  #The number of LEDs on the ring.
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels,brightness = brightness,pixel_order = neopixel.GRBW,auto_write = True)  #Set up the neopixel object.    
    return pixels

#Function that defines LED colors.
def neopixel_color(pixels,color = 'white'):  #Default color is white.
    if color == 'red':  #If the user selects a color...
        pixels.fill((255, 0, 0, 0))  #...issue the RGBW values.
    elif color == 'green':
        pixels.fill((0, 255, 0, 0))
    elif color == 'blue':
        pixels.fill((0, 0, 255, 0))
    elif color == 'white':
       pixels.fill((0, 0, 0, 255))
    elif color == 'blank':
       pixels.fill((0,0,0,0))
    else:
       pixels.fill((0, 0, 0, 255))   #Default to displaying the color white if an invalid color is entered.
    #pixels.show()  #Turn on the LEDs. Not needed if auto_write = True under the pixels object.
    return


if __name__ == "__main__":  
    main()  #After functions are read in, run the main function.








#--------------------------Legacy------------------------------#

#Legacy function that determines the HDMI power state.
def power_hdmi(state):
    if state == 'off':
        os.system("sudo /usr/bin/tvservice -o")
        os.system("sudo /opt/vc/bin/tvservice -o")
    elif state == 'on':
        os.system("sudo /usr/bin/tvservice -p")
        os.system("/opt/vc/bin/tvservice -p")
    else:
        os.system("sudo /usr/bin/tvservice -p")  #Default to turning the HDMI on in case I can't type.
        os.system("sudo /opt/vc/bin/tvservice -p")
    return

#Legacy function that determines the WiFi txpower state.
def power_wifi(state):
    if state == 'off':
        os.system("sudo iwconfig wlan0 txpower off")
    elif state == 'on':
        os.system("sudo iwconfig wlan0 txpower auto")
    else:
        os.system("sudo iwconfig wlan0 txpower auto")  #Default to turning the WiFi on in case I can't type.
    return

#Legacy function that determines ACT LED state.
def power_act_led(state):
    if state == 'off':
        os.system("echo none | sudo tee /sys/class/leds/led0/trigger")
        os.system("echo 1 | sudo tee /sys/class/leds/led0/brightness")
    elif state == 'on':
        os.system("echo heartbeat | sudo tee /sys/class/leds/led0/trigger")
        os.system("echo 0 | sudo tee /sys/class/leds/led0/brightness")
    else:
        os.system("echo 0 | sudo tee /sys/class/leds/led0/brightness") #Default to keeping the ACT LED on.
    return

#--------------------------------------------------------#


