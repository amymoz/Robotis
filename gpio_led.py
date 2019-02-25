import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BOARD)

def map(x,in_min,in_max,out_min,out_max):
    return (x - in_min)/(in_max-in_min)*(out_max-out_min)+out_min

def set_servo(pin,degree):
    degree = map(degree+90,0,180,2.5,11)
    print(degree)
    GPIO.setup(pin, GPIO.OUT)
    pwm_servo = GPIO.PWM(pin, 50)
    pwm_servo.start(2.5)
    pwm_servo.ChangeDutyCycle(degree)
    sleep(0.5)
    GPIO.cleanup(pin)

while True:
  set_servo(12,int(input("servo ==> ")))
