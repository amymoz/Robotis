#!/usr/bin/python

# Take photo in low light situation

import picamera
import time
from fractions import Fraction

camera = picamera.PiCamera() 
camera.resolution = (640, 480)
camera.framerate = Fraction(1, 6)
camera.shutter_speed = 6000000
camera.iso = 800 
time.sleep(30)
camera.exposure_mode = 'off'
camera.capture('dark.jpg')
