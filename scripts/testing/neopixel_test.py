'''
Description
This is a script for testing an Adafruit Neopixel RGBW Ring on a Raspberry Pi.
Tested on the RPi4 and RPiZero without other peripherals hooked up.

Pinout: 
    RPi - Neopixel
    5v - 5v
    GND - GND
    MOSI - Data Input

Issue:
Flickering occasionally occurs while holding colors. 
This may be due to using the MOSI line, so when utilizing an appropriate GPIO, the user should run the script with sudo.

Author: iblack
Date: 2020-03-23
'''
import os, time #Used for resetting and pausing the script. 
import board, neopixel  #Used for the Neopixel.

def main():
    pixels = neopixel_setup(num_pixels = 16, brightness = 1)  #Set up the neopixel object.
    neopixel_color(pixels,color = 'blank') #Turn off the LEDs.
	time.sleep(3)
    neopixel_color(pixels,color = 'blue')  #Blue LEDs for 30 seconds.
	time.sleep(5)
	neopixel_color(pixels,color = 'red')  #Blue LEDs for 30 seconds.
	time.sleep(5)
    neopixel_color(pixels,color = 'green')  #Blue LEDs for 30 seconds.
	time.sleep(5)
	neopixel_color(pixels,color = 'white')  #Blue LEDs for 30 seconds.
    time.sleep(5)
    neopixel_color(pixels,color = 'blank')  #Blue LEDs for 30 seconds.
	os._exit(00)  #Reset the IPython console.
	return print("Console reset.")

def neopixel_setup(num_pixels,brightness = 1):
    pixel_pin = board.D10  #Define the data input pin for the Pi.
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels,brightness = brightness,pixel_order = neopixel.GRBW)  #Set up the neopixel object.    
    return pixels

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
    pixels.show()  #Turn on the LEDs.
    return

if __name__ == "__main__":  
    main()  #After functions are read in, run the main function.
