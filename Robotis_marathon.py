from time import sleep
import cv2
import numpy as np

from Methods import *
from rasp_Methods import *

minf = np.array([20,169,63])
maxf = np.array([71,255,182])

contours = {}
center = {}

deltadt = 0.1
dt1 = 4
dt2 = 6

while True:
    shib = 0

    frame = {}
    frame['org'] = vs.read()
    frame['left'] = frame['org'][ yframe//4 : yframe-yframe//4 , 0: xframe//4 ] 
    frame['right'] = frame['org'][ yframe//4 : yframe-yframe//4 , (xframe//4)*3 : xframe] 
    frame['top'] = frame['org'][ 0:yframe//4, 0:xframe]
    frame['bottom'] = frame['org'][ yframe//4 *3 : yframe, 0 : xframe]
    

    for d in frame.keys():
        contours[d] = cv2.cvtColor(frame[d], cv2.COLOR_BGR2HSV)
        contours[d] = cv2.GaussianBlur(contours[d], (5, 5), 0)
        contours[d] = cv2.inRange(contours[d], minf, maxf)
        contours[d] = cv2.medianBlur(contours[d], 25)
        contours[d] = cv2.findContours(contours[d],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]
    
    #filteredfr = cv2.bitwise_and(frame['org'],frame['org'], mask= medianedfr)

    try:  
        if len(contours['org']) > 0:
            contours['org'] = max(contours['org'], key=cv2.contourArea)
            (xfr,yfr) = cv.minEnclosingCircle(contours['org'])
            #xfr,yfr,wfr,hfr = cv2.boundingRect(contours['org'])
            #cv2.rectangle(frame['org'],(xfr,yfr),(xfr+wfr,yfr+hfr),(0,255,0),2)
            for f in contours.keys()[1:5]:
                if (len(contours[f])>0):
                    contours[f] = max(contours[f], key = cv2.contourArea)
                    (xcnt,ycnt) = cv2.minEnclosingCircle(contours[f])     
                    errx = xcenter - xcnt
                    erry = ycenter - ycnt
                    center[f] = [errx,erry]
            
            if (xfr) > xcenter + 100:
                khat = 'rast'
            elif (xfr) < xcenter - 100:
                khat = 'chap'
            elif (xfr) < (xcenter + 100) and xfr > (xcenter - 100):
                khat = 'markaz'
            
            if(isinstance(center['left'], list) and isinstance(center['right'], list)):
                shib = (center['left'][1]-center['right'][1]) / (center['left'][0] - center['right'][0])
            elif(isinstance(center['left'], list) and isinstance(center['top'], list)):
                shib = (center['left'][1]-center['top'][1]) / (center['left'][0] - center['top'][0])
            elif(isinstance(center['left'], list) and isinstance(center['bottom'], list)):
                shib = (center['left'][1]-center['bottom'][1]) / (center['left'][0] - center['bottom'][0])
            elif(isinstance(center['right'], list) and isinstance(center['top'], list)):
                shib = (center['right'][1]-center['top'][1]) / (center['right'][0] - center['top'][0])
            elif(isinstance(center['right'], list) and isinstance(center['bottom'], list)):
                shib = (center['right'][1]-center['bottom'][1]) / (center['right'][0] - center['bottom'][0])
            elif(isinstance(center['top'], list) and isinstance(center['bottom'], list)):
                shib = (center['top'][1]-center['bottom'][1]) / (center['top'][0] - center['bottom'][0])
            print(shib)
            print(khat)
            
    except Exception as excerr:
        prexcerr)
