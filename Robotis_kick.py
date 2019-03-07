import numpy as np
import cv2
from rasp_Methods import *

#minf = np.array([25,255,95])
#maxf = np.array([40,255,255])
minf = np.array([29,81,0])#[",80<smin<170,"]
maxf = np.array([62,255,255])
fails = 0

#actions = ['Soccer_Pass_Left','Soccer_Pass_Right','Soccer_Shoot_Right']

while True:
    try:
        frame = vs.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        binary = cv2.inRange(hsv, minf, maxf)
        blured = cv2.medianBlur(binary, 25)  
        filterd = cv2.bitwise_and(frame,frame, mask= blured)
        contour = cv2.findContours(blured,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]
        xcontour, ycontour = None, None
        if len(contour) > 0:
            contour = max(contour, key = cv2.contourArea)
            (xcontour,ycontour) = cv2.minEnclosingCircle(contour)[0]
            errx = xcontour - xcenter
            erry = ycontour - ycenter
            #y_pos = set_servo(servo_y ,y_pos + ( 0.05 * erry) )
            if ycontour > 240:
                play_action('Soccer_Forward')
            elif ycontour < 240:
                play_action('Soccer_Forward')
                play_action('Soccer_Forward')
                play_action('Soccer_Shoot_Right')
#            if errx >= 50 and errx <= 150:
#                rob.robo_play = 'Soccer_Forward_Right'
#            elif errx <= -50 and errx >= -150:
#                rob.robo_play = 'Soccer_Forward_Left'
#            elif errx > 150:
#                rob.robo_play = 'Soccer_Turn_Right'
#            elif errx < -150:
#                rob.robo_play = 'Soccer_Turn_Left'
#            else:
#                rob.robo_play = 'Soccer_Forward'

        cv2.imshow('frame', filterd)
        ss= cv2.waitKey(1)
        if ss == ord('q'):
            break
    except :
        if fails > 5 :
            rob.robo_play = 'Soccer_Turn_Right'
            fails = 0
        else: 
            fails += 1
