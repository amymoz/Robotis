from os import system
from time import sleep
import cv2
from Methods import *

excel_file = "Book.xlsx"

dxl.enable_torque(fids)

#releases=[17,18,9,10,1,2,3,4,5,6]
res = (-81.67, 81.09, -68.48, 55, -14.52, 13.64, -46.19, 44.72, -3.37, 15, -46.77, 55.28, -73.75, 90.76, 36.51, -46.19, 20, 9.24)
set_pos(res)

cv2.namedWindow('window')
#while True:
#    for i in range(1,86):
#        mm = motion(excel_file)
#        set_pos(mm[i])
#        sleep(float(mm[i][18]))
while True:
    prt("Inter number of servo==> ",end='')
    fid=''
    while True:
        out = cv2.waitKeyEx(0)
        if (out < 58 and out > 47):
            st = str(int(out)-48)
            fid += st
            prt(st , end='')
        elif (out == 13):
            break
    fid = int(fid)
    prt("\nchange value with (2 Up and 0 Down) for servo({0})...then press enter".format(fid),end='')
    while True :
        key=cv2.waitKeyEx(0)
        pos=float(get_pos()[(fid-1)])
        if (key == 50):
            pos += 2
        elif (key == 48):
            pos -= 2
        elif (key == 13):
            break
        dxl.set_goal_position({fid:pos})
    system("clear")

dxl.disable_torque(fids)