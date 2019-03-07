#!/usr/bin/python

import picamera
import time

camera = picamera.PiCamera()
time.sleep(2)    # Camera warm-up time
camera.capture('test.jpg') #, use_video_port=True)
