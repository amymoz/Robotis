#!/usr/bin/python3
from os import system
from time import *
from Methods import *

import threading
import cv2
import apriltag

cap = cv2.VideoCapture(2)
detector = apriltag.Detector()
#cv2.namedWindow('frame')

Start_Dynamixel()

thread = []
robo_play = ['','']

while True :
    frame = cap.read()[1]
    detect_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detect_data, detect_img = detector.detect(detect_img, return_image=True)
    frame_size = ( len(frame[0]) , len(frame) )
    frame_center = ( frame_size[0] // 2 , frame_size[1] // 2 )

    try:
        april_x = detect_data[0][6][0]
        shoudgo = (april_x - frame_center[0]) // 3
        
        if shoudgo < 0 :
            robo_play[1] = 'Soccer_Forward_Left'
        elif shoudgo > 0 :
            robo_play[1] = 'Soccer_Forward_Right'
        else:
            robo_play[1] = 'Soccer_Forward'
        
        if shoudgo > 50 :
            robo_play[1] = 'Soccer_Turn_Right'
        if shoudgo < -50 :
            robo_play[1] = 'Soccer_Turn_Left'

        #print(detect_data[0].tostring())
    except:
        robo_play[1] = 'Soccer_Balance'
    
    if (robo_play[0] != robo_play[1] ) :
        if len(thread)>0:
            thread[0]._stop()
    else:
        continue
    #overlay = frame // 2 + detect_img[:, :, None] // 2
    #cv2.imshow('frame', overlay)
    #cv2.waitKey(1)
    
    t = threading.Thread(target=play_action,args=(robo_play[1]))
    thread.append(t)
    t.start()
    
    robo_play[0] = robo_play[1]
    robo_play[1] = ''
    
