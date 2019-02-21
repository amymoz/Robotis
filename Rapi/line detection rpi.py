from imutils.video import VideoStream
import imutils
import numpy as np
import cv2 as cv
import RPi.GPIO as rp
from time import sleep

def map( x, in_min,in_max, out_min, out_max):
    maps = -((x - in_max)*(out_max-out_min)/(in_max-in_min)+out_min)
    return maps
def nothing(x):
    pass 

minf = np.array([20,169,63])
maxf = np.array([71,255,182])

hsv = [0,0,0,0]
hsvblured = [0,0,0,0]
binary = [0,0,0,0]
medianed = [0,0,0,0]
im2 = [0,0,0,0]
contours = [0,0,0,0]
hierarchy = [0,0,0,0]
window = ['wcp1','wcp2','wcp3','wcp4']
window2 = ['wccp1','wccp2','wccp3','wccp4']
window3 = ['wcccp1','wcccp2','wcccp3','wcccp4']

servo1 = 15
servo2 = 14
deltadt = 0.1
dt1 = 4
dt2 = 6

rp.setmode(rp.BCM)
rp.setwarnings(False)
rp.setup(servo1,rp.OUT)
rp.setup(servo2,rp.OUT)
pwm1 = rp.PWM(servo1,50)
pwm2 = rp.PWM(servo2,50)
pwm1.start(2)
pwm2.start(7)

cv.namedWindow('frame',cv.WINDOW_FREERATIO)
usingPiCamera = True
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=(240, 240),
	framerate=60).start()
sleep(0.2) 
pwm1.stop()
pwm2.stop()
################################################################################################################################	
while True:
    frame = vs.read()
    if not usingPiCamera:
	    frame = imutils.resize(frame, width=frameSize[0])
    
    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)
    xframe = len(frame[0])
    yframe = len(frame)
    ycnt = [0,0,0,0]
    xcnt = [0,0,0,0]
    cnt = [0,0,0,0]
    radius = [0,0,0,0]
    center = [0,0,0,0]
    cnter = [0,0,0,0]
    shib = 0

    cropped = [frame[int(yframe/4):int(yframe-yframe/4), 0:int(xframe/4)] , frame[int(yframe/4):int(yframe-yframe/4), int((xframe/4)*3):xframe] , frame[0:int(yframe/4), 0:xframe] , frame[int((yframe/4)*3):yframe, 0:xframe] ]
    hsvfr = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsvbluredfr = cv.GaussianBlur(hsvfr, (5, 5), 0)
    binaryfr = cv.inRange(hsvbluredfr, minf, maxf)
    medianedfr = cv.medianBlur(binaryfr, 25)
    filteredfr = cv.bitwise_and(frame,frame, mask= medianedfr)
    im2fr, contoursfr, hierarchyfr = cv.findContours(medianedfr,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for d in range(0,4):
        hsv[d] = cv.cvtColor(cropped[d], cv.COLOR_BGR2HSV)
        hsvblured[d] = cv.GaussianBlur(hsv[d], (5, 5), 0)
        binary[d] = cv.inRange(hsvblured[d], minf, maxf)
        medianed[d] = cv.medianBlur(binary[d], 25)
        im2[d], contours[d], hierarchy[d] = cv.findContours(medianed[d],cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)  

    try:  
        if len(contoursfr) > 0:
            cntfr = max(contoursfr, key = cv.contourArea)
            (xfr,yfr), radiusfr = cv.minEnclosingCircle(cntfr) 
            centerfr = (int(xfr),int(yfr)) 
            cv.circle(frame,centerfr,2,(255,0,0),2)
            xfr,yfr,wfr,hfr = cv.boundingRect(cntfr)
            cv.rectangle(frame,(xfr,yfr),(xfr+wfr,yfr+hfr),(0,255,0),2)
            for f in range (0,4):
                if (len(contours[f])>0):
                    cnt[f] = max(contours[f], key = cv.contourArea)
                    (xcnt[f],ycnt[f]), radius[f] = cv.minEnclosingCircle(cnt[f])     
                    cnter[f] = (int(xcnt[f]),int(ycnt[f]))
                    errx = mrkzx - int(xcnt[f])
                    erry = mrkzy - int(ycnt[f])
                    center[f] = [errx,erry]
                    radius[f] = int(radius[f])
                    cv.circle(cropped[f],cnter[f],radius[f],(0,0,255),2)
                    cv.circle(cropped[f],cnter[f],2,(255,0,0),2)   
            if (int(xcnt[f]) > mrkzx + 100):
                khat = 'rast'
            elif (int(xcnt[f]) < mrkzx - 100):
                khat = 'chap'
            elif (int(xcnt[f]) < int((mrkzx + 100)) and int(xcnt[f]) > int((mrkzx - 100)) ):
                khat = 'markaz'
            if(isinstance(center[0], list) and isinstance(center[1], list)):
                shib = (center[0][1]-center[1][1]) / (center[0][0] - center[1][0])
            elif(isinstance(center[0], list) and isinstance(center[2], list)):
                shib = (center[0][1]-center[2][1]) / (center[0][0] - center[2][0])
            elif(isinstance(center[0], list) and isinstance(center[3], list)):
                shib = (center[0][1]-center[3][1]) / (center[0][0] - center[3][0])
            elif(isinstance(center[1], list) and isinstance(center[2], list)):
                shib = (center[1][1]-center[2][1]) / (center[1][0] - center[2][0])
            elif(isinstance(center[1], list) and isinstance(center[3], list)):
                shib = (center[1][1]-center[3][1]) / (center[1][0] - center[3][0])
            elif(isinstance(center[2], list) and isinstance(center[3], list)):
                shib = (center[2][1]-center[3][1]) / (center[2][0] - center[3][0])
            print(shib)
            print(khat)
    except Exception as excerr:
        print(excerr)
################################################
    for i in range(0,4):
        #cv.imshow(window[i], cropped[i])
        cv.imshow("frame", frame)    
############################################################################################################
    ikey = cv.waitKey(1)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        pwm1.stop()
        pwm2.stop()
        rp.cleanup()
        vs.stop()
        break
