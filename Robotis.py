#!/usr/bin/python3
from time import *
from os import system
import threading
import cv2
import apriltag
from imutils.video import VideoStream
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#frameSize = (320, 240)
#frameSize = (1296, 730)
#frameSize = (1920, 1080)
#frameSize = (2592, 1944)
#frameSize = (1296, 972)
frameSize = (640, 480)

vs = VideoStream(src=0, usePiCamera=True, resolution=frameSize, framerate=20).start()
from Methods import *

def map(x,in_min,in_max,out_min,out_max):
    return (x - in_min)/(in_max-in_min)*(out_max-out_min)+out_min

servo_x = 12
#servo_y = 
def set_servo(pin,degree):
    degree = map(degree,0,180,2.5,11)  +90 # 90 is 0 front
    GPIO.setup(pin, GPIO.OUT)
    pwm_servo = GPIO.PWM(pin, 50)
    pwm_servo.start(2.5)
    pwm_servo.ChangeDutyCycle(degree)
    sleep(0.5)
    GPIO.cleanup(pin)
    return degree

detector = apriltag.Detector()

global robo_play
robo_play = ['', 'Soccer_Balance']

def play_live():
    while True:
        play_action(robo_play[1])
threading.Thread(target=play_live).start()

fails = 0
x_pos = 0

while True :
    frame = vs.read()
    detect_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_data, detect_img = detector.detect(detect_img, return_image=True)
    frame_size = ( len(frame[0]), len(frame) )
    frame_center = ( frame_size[0] // 2 , frame_size[1] // 2 )
    
    try:
        april_x = (detect_data[0][6][0] - frame_center[0]) // 3 
        fails = 0

        elif april_x > 0:
            x_pos = set_servo(servo_x, x_pos -1 )
        elif april_x < 0:
            x_pos = set_servo(servo_x, x_pos +1 )
        
        if x_pos > 10 and x_pos < 30

    except:
        if fails > 10 :
#            if robo_play[0].count("Right"):
#                servo_x_pos = set_servo(servo_x,servo_x_pos -5 )
#            elif robo_play[0].count("Left"):
#                servo_x_pos = set_servo(servo_x,servo_x_pos +5 )
#
#            robo_play[0] = robo_play[1] if robo_play[0] != robo_play[1]

#        robo_play[1] = 'Soccer_Turn_Left'
#        robo_play[1] = 'Soccer_Turn_Right'
#        robo_play[1] = 'Soccer_Forward_Right'
#        robo_play[1] = 'Soccer_Forward_Left'
#        robo_play[1] = 'Soccer_Forward'
            robo_play[1] = 'Soccer_Balance'
            fails = 0
        else : 
            fails += 1
    
    #print(robo_play)
    #overlay = frame // 2 + detect_img[:, :, None] // 2
    #cv2.imshow('frame', overlay)
    #cv2.waitKey(1)
    
cv2.destroyAllWindows()
vs.stop()
