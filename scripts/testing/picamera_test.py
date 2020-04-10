import time
import picamera
from datetime import datetime

directory = r'C:\Users\Ian\Desktop'

identifier = input('Enter identifier for video: ')  #Prepend the file with a user-entered text string.
dnt = datetime.now().strftime("%Y-%m-%d_%H%M") #Get the current date and time in the format of yyyy-mm-dd_HH:MM.
filetype = '.h264' #File extension of the video.
filename = identifier + '_' + dnt + filetype  #Generate the filename.
time.sleep(1)  #Wait one second.

camera = picamera.PiCamera(resolution = (1920, 1080), framerate = 30) #Set the camera resolution to 720p at 30fps.
camera.start_recording(filename)  #Name the output file the generated filename.
camera.wait_recording(5)  #Wait five seconds for any errors to pop up.
print('Beginning recording.')
camera.preview_fullscreen = False  
camera.preview_window = (1200,0,640,480)  #Format: Xpos, Ypos, Height, Width
camera.start_preview()  
camera.wait_recording(30)
camera.stop_preview()
camera.stop_recording()
print('Test recording complete.')

