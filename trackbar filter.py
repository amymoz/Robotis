import cv2 as cv
import numpy as np
from rasp_Methods import *

def nothing():
    pass
cv.namedWindow('window',cv.WINDOW_NORMAL)
cv.createTrackbar('hmin', 'window',0,255,nothing)
cv.createTrackbar('hmax', 'window',0,255,nothing)
cv.createTrackbar('smin', 'window',0,255,nothing)
cv.createTrackbar('smax', 'window',0,255,nothing)
cv.createTrackbar('vmin', 'window',0,255,nothing)
cv.createTrackbar('vmax', 'window',0,255,nothing)
cv.setTrackbarPos('hmax', 'window',255)
cv.setTrackbarPos('smax', 'window',255)
cv.setTrackbarPos('vmax', 'window',255)

while True:
    frame = cap.read()[1]
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    hmin = cv.getTrackbarPos('hmin','window')
    smin = cv.getTrackbarPos('smin','window')
    vmin = cv.getTrackbarPos('vmin','window')
    hmax = cv.getTrackbarPos('hmax','window')
    smax = cv.getTrackbarPos('smax','window')
    vmax = cv.getTrackbarPos('vmax','window')

    minfr = np.array([hmin, smin, vmin])
    maxfr = np.array([hmax, smax, vmax])
    moz = cv.inRange(hsv, minfr, maxfr)
    mooz = cv.bitwise_and(frame, frame, mask=moz )
#################################################################
    cv.imshow('window',mooz)
    ss = cv.waitKey(1)
    if (ss == ord('q')):
        break
cv.destroyAllWindows()