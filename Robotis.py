from os import system
from time import sleep
import cv2
from Methods import *

poss_file = "/media/Game/Professional/Project/GitArch/Robotis/poss.txt"
frames = motion_file(poss_file)
dxl.enable_torque(fids)
set_speed(200)

cv2.namedWindow('window')
dicts={}
for i in range(0,len(fids)):
    dicts[fids[i]]=True
dxl.set_force_control_enable(dicts)

fid=str(fids[0])
pos=0
np=''
def tec():

    dxl.set_goal_position({int(fid):pos})
def home():
    system("clear")
    print(fids)
while True:
    home()
    while True :
        pos=float(get_pos()[(int(fid)-1)])
        prt("\033[2K\033[0Gchange value with [w](Up) [s](Down) for servo( {} : {} ) or enter degree... then press enter ==> {}".format(fid,pos,np),end='')
        key=cv2.waitKey(0)
        if (key < 58 and key > 47):
            np += chr(int(key))
        elif (key == 8):
            np = np[:len(np)-1]
        elif (key == ord('-')):
            np = '-'
        elif (key == ord('d')):
            print('')
            while True:
                prt("\033[2K\033[0GInter servo id==> {}".format(fid),end='')
                out = cv2.waitKey(0)
                if (out < 58 and out > 47):
                    fid += str(int(out)-48)
                elif (out == 8):
                    fid = fid[:len(fid)-1]
                elif (out == 13):
                    break
            home()
        elif (key == ord('f')):
            frm=''
            print('')
            while True:
                prt("\033[2K\033[0GInter frame id==> {}".format(frm),end='')
                out = cv2.waitKeyEx(0)
                if (out < 58 and out > 47):
                    frm += chr(int(out))
                elif (out == ord(',')):
                    frm += ','
                elif (out == 8):
                    frm = frm[:len(frm)-1]
                elif (out == 13):
                    break
            frm = str(frm).split(',')
            for i in range(len(frm)):
                frm[i] = int(frm[i])-1
            set_pos(frames[frm[0]][frm[1]])
            home()
        elif (key == ord('p')):
            play_frames(frames,[31])
            sleep(2)
            play_frames(frames,[32,33])
            while True:
                play_frames(frames,[38,39,36,37])
                #sleep(0.1)
                
        elif (key == ord('w')):
            pos += float(2)
            tec()
        elif (key == ord('s')):
            pos -= float(2)
            tec()
        elif (key == 13 and np != ''):
            pos = float(np)
            tec()
            np=''
        elif (key == 13):
            break
dxl.disable_torque(fids)
