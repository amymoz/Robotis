import apriltag
import cv2

frame = cv2.imread('/media/root/Game/Professional/Project/GitArch/Robotis/aprilimg.jpg')
frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
detector = apriltag.Detector()

result,img = detector.detect(frame,return_image=True)
overlay = frame // 2 + img // 2
cv2.imshow('s1',frame)
cv2.imshow('s2',overlay)
cv2.waitKey(4000)
