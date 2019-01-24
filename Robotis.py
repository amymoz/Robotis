from os import system
from time import sleep
import cv2
from Methods import *

excel_file = "Book.xlsx"

dxl.enable_torque(fids)

#releases=[17,18,9,10,1,2,3,4,5,6]
#res = (-81.67, 81.09, -68.48, 55, -14.52, 13.64, -46.19, 44.72, -3.37, 15, -46.77, 55.28, -73.75, 90.76, 36.51, -46.19, 20, 9.24)
#set_pos(res)

#poss=[8,15,51,58,37,44]
poss=[8,15,15,79,51,58,58,65,37,44,44,79]
for i in poss[0:4]:
    mm = motion(excel_file)
    set_pos(mm[i])
    sleep(0.20)
while True:
    for i in poss[4:]:
        mm = motion(excel_file)
        set_pos(mm[i])
        sleep(0.20)
    #    sleep(1)
        #sleep(float(mm[i][18]))
cv2.namedWindow('window')
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
    prt("\nchange value with (2 Up and 0 Down) for servo({0})...then press enter\n".format(fid),end='')
    while True :
        key=cv2.waitKeyEx(0)
        pos=float(get_pos()[(fid-1)])
        if (key == 50):
            pos += float(2)
        elif (key == 48):
            pos -= float(2)
        elif (key == 13):
            break
        dxl.set_goal_position({fid:pos})
        print(get_pos())
    system("clear")

dxl.disable_torque(fids)