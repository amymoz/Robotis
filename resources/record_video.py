#!/usr/bin/python

import picamera

camera = picamera.PiCamera()
camera.start_recording('video.h264')
camera.wait_recording(10)
camera.stop_recording()
