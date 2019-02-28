from time import sleep
import RPi.GPIO as GPIO
from imutils.video import VideoStream
import threading
from Methods import *
        
def map(x,in_min,in_max,out_min,out_max):
    return (x - in_min)/(in_max-in_min)*(out_max-out_min)+out_min

def set_servo(pin,degree):
    degree2 = map(degree,-90,90,2.5,11) # 90 is 0 front
    GPIO.setup(pin, GPIO.OUT)
    pwm_servo = GPIO.PWM(pin, 50)
    pwm_servo.start(2.5)
    pwm_servo.ChangeDutyCycle(degree2)
    sleep(0.2)
    GPIO.cleanup([pin])
    return degree

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#frameSize = (320, 240) (1296, 730) (1920, 1080) (2592, 1944) (1296, 972)

xframe,yframe = 480,640
xcenter,ycenter = xframe // 2 , yframe // 2

vs = VideoStream(src=0, usePiCamera=True, resolution=(yframe,xframe), framerate=20).start()
class rob:
    robo_play = 'Soccer_Balance'

servo_x,servo_y = 12,35

fails = 0

x_pos = set_servo(servo_x,0)
y_pos = set_servo(servo_y,-50)

def play_live():
    while True:
        play_action(rob.robo_play)
threading.Thread(target=play_live).start()
