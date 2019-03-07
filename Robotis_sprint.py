#!/usr/bin/python3
import cv2
from rasp_Methods import *
from Methods import *
import threading
import numpy as np

global wait_it
global xcontour
global ycontour

wait_it = True
xcontour= 0
ycontour= 0

def detect_it():
    global wait_it
    global xcontour
    global ycontour
    minf = np.array([27,34,0])
    maxf = np.array([43,148,255])

    while True:
        frame = cap.read()[1]
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        binary = cv2.inRange(hsv, minf, maxf)
        blured = cv2.medianBlur(binary, 25)
        contour = cv2.findContours(blured,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]
        filterd = cv2.bitwise_and(frame,frame, mask= blured)
        if len(contour) > 0:
            contour = max(contour, key = cv2.contourArea)
            xcontour, ycontour = cv2.minEnclosingCircle(contour)[0]
        else:
            xcontour, ycontour = 0,0

        wait_it = False

        #cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        #cv2.imshow('frame', filterd)
        #cv2.imshow('frame1', frame)
        #cv2.waitKey(1)
threading.Thread(target=detect_it).start()

last_robo = ''
fails = 0

while True :
    while wait_it:
        pass
    wait_it = True
    if xcontour == 0:
        fails += 1
        if fails > 10 :
            if last_robo == 'L':
                print(last_robo , 'L')
                play_action('Soccer_Turn_Right')
            if last_robo == 'R':
                print(last_robo,'R')
                play_action('Soccer_Turn_Left')
        continue
    print(xcontour)
    print(fails)
    if xcontour >  ( 4/5 * xframe):
        print('Soccer_Turn_Right')
        last_robo = 'R'
        play_action('Soccer_Turn_Right')
    elif xcontour < ( 1/5 * xframe):
        print('Soccer_Turn_Left')
        last_robo = 'L'
        play_action('Soccer_Turn_Left')
    else:
        print('Soccer_Forward')
        last_robo = 'L'
        play_action('Soccer_Forward')

