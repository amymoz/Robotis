from __future__ import division
from __future__ import print_function
from argparse import ArgumentParser
import cv2 as cv
import apriltag
###/################################
webcam = cv.VideoCapture(0)
cv.namedWindow('window')
tagid = 8  
####################################
parser = ArgumentParser(description='test apriltag Python bindings')
parser.add_argument('device_or_movie', metavar='INPUT', nargs='?', default=0,help='Movie to load or integer ID of camera device')
apriltag.add_arguments(parser)
options = parser.parse_args()
detector = apriltag.Detector(options,searchpath=apriltag._get_demo_searchpath())
###/################################
while True:
    _, frame = webcam.read()
    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)
    xframe = len(frame[0])
    yframe = len(frame)

    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    detections, dimg = detector.detect(gray, return_image=True)
    hilight = frame // 2 + dimg[:, :, None] // 2 

######################################################################
    try:
        # inja to kode asli if ddm ke age id yeki bud x va y ro bgire va...
        print(detections)    
        
######################################################################
    except Exception as error:
        print(error)
################################### 
    cv.imshow('window', hilight)
    #cv.imshow('frame', frame)
###################################
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
