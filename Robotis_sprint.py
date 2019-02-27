#!/usr/bin/python3
from time import *
from os import system
import threading
import cv2
import apriltag
from imutils.video import VideoStream
import RPi.GPIO as GPIO

tagid = 0
servo_x,servo_y = 12,35

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#frameSize = (320, 240) (1296, 730) (1920, 1080) (2592, 1944) (1296, 972)
frameSize = (640, 480)

vs = VideoStream(src=0, usePiCamera=True, resolution=frameSize, framerate=20).start()
from Methods import *
from rasp_Methods import *

x_pos = set_servo(servo_x,0)
y_pos = set_servo(servo_y,-50)

global robo_play
robo_play = ['', 'Soccer_Balance']
fails = 0
detector = apriltag.Detector()

def play_live():
    while True:
        play_action(robo_play[1])
threading.Thread(target=play_live).start()


while True :
    frame = vs.read()
    detect_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_data, detect_img = detector.detect(detect_img, return_image=True)
    
    frame_size = ( len(frame[0]), len(frame) )
    frame_center = ( frame_size[0] // 2 , frame_size[1] // 2 )

    found_tag = False
    for L in range (len(detect_data)):
        found_tag = False
        if detect_data[L][1] == 0:
            detect_data = detect_data[L]
            found_tag = True
    if found_tag  == False:
        detect_data = None
    
    try:
        april_x = (detect_data[6][0] - frame_center[0]) // 5
        april_y = (detect_data[6][1] - frame_center[0]) // 5
        fails = 0
        
        if april_x > 15:
            x_pos = set_servo(servo_x, x_pos - 5)
        elif april_x < -15:
            x_pos = set_servo(servo_x, x_pos + 5)

        if april_y > 15:
            y_pos = set_servo(servo_y, y_pos - 5)
        elif april_y < -15:
            y_pos = set_servo(servo_y, y_pos + 5)

        if x_pos >= 15 and x_pos <= 35:
            robo_play[1] = 'Soccer_Forward_Right'
        if x_pos <= -15 and x_pos >= -35:
            robo_play[1] = 'Soccer_Forward_Left'
        if x_pos > 35:
            robo_play[1] = 'Soccer_Turn_Right'
        if x_pos < -35:
            robo_play[1] = 'Soccer_Turn_Left'
        else:
            robo_play[1] = 'Soccer_Forward'
    except:

#        if fails > 10 :
#            if robo_play[0].count("Right"):
#                servo_x_pos = set_servo(servo_x,servo_x_pos -5 )
#            elif robo_play[0].count("Left"):
#                servo_x_pos = set_servo(servo_x,servo_x_pos +5 )
#
#            robo_play[0] = robo_play[1] if robo_play[0] != robo_play[1]
#
#
#            robo_play[1] = 'Soccer_Balance'
#            fails = 0
#        else : 
#            fails += 1
        pass

    #overlay = frame // 2 + detect_img[:, :, None] // 2
    #cv2.imshow('frame', overlay)
    #cv2.waitKey(1)
    
GPIO.cleanup()
cv2.destroyAllWindows()
vs.stop()
