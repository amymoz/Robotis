#!/usr/bin/python3
import time
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils

usingPiCamera = True
frameSize = (640, 480)

vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize, framerate=30).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    if not usingPiCamera:
        frame = imutils.resize(frame, width=frameSize[0])

    cv2.imshow('orig', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
