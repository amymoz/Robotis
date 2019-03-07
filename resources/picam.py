from picamera import PiCamera
from time import sleep


camera = PiCamera()

#camera.resolution = 

camera.start_preview()
sleep(50)

camera.stop_preview()

