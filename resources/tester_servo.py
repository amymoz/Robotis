import RPi.GPIO as GPIO
from time import *
from rasp_methods import *

GPIO.setmode(GPIO.BOARD)
pin = int(input('input pin in GPIO.BOARD mode ==> '))
while True:
  set_servo(pin,int(input("servo ==> ")))
