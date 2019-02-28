#!/usr/bin/python3
import cv2
import apriltag
from rasp_Methods import *

tagid = 4
detector = apriltag.Detector()

def detect_it():
    frame = vs.read()
    detect_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_data, detect_img = detector.detect(detect_img, return_image=True)
    #try:
        #detect_data = detect_data[0]
    for L in range (len(detect_data)):
        if detect_data[L][1] == tagid:
            detect_data = detect_data[L]
    #except:
    #    pass
    #overlay = frame // 2 + detect_img[:, :, None] // 2
    #cv2.imshow('frame', overlay)
    #cv2.waitKey(1)
    if isinstance(detect_data,list):
        detect_data = None
    return detect_data

while True :
    try:
        detect_data = detect_it()
        april_x = (detect_data[6][0] - xcenter)
        fails = 0
        if april_x >= 50 and april_x <= 150:
            rob.robo_play = 'Soccer_Forward_Right'
        if april_x <= -50 and april_x >= -150:
            rob.robo_play = 'Soccer_Forward_Left'
        if april_x > 150:
            rob.robo_play = 'Soccer_Turn_Right'
        if april_x < -150:
            rob.robo_play = 'Soccer_Turn_Left'
        else:
            rob.robo_play = 'Soccer_Forward'

    except:
        if fails > 10 :
            rob.robo_play = 'Soccer_Turn_Right'
            fails = 0
        else: 
            fails += 1
