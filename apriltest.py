import apriltag
import cv2
img = cv2.imread('/media/root/Game/Professional/Project/GitArch/Robotis/aprilimg.jpg',cv2.IMREAD_GRAYSCALE)
detector = apriltag.Detector()

result = detector.detect(img)
cv2.imshow('sss',cv2.Canny(img,0,10))
cv2.waitKey(0)
