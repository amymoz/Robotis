#!/usr/bin/python3
from os import system
from time import sleep
import cv2
from Methods import *

#poss_file = "/media/root/Game/Professional/Project/GitArch/Robotis/poss2.txt"
poss_file = "/media/root/Game/Professional/Project/GitArch/Robotis/noname.mtnx"
frames = motion_file(poss_file)
dxl.enable_torque(fids)

set_speed(100)

cv2.namedWindow('window')
dicts={}
for i in range(0,len(fids)):
    dicts[fids[i]]=True
dxl.set_force_control_enable(dicts)

fid=str(fids[0])
pos=0
u_input=''

def update_pos():
    dxl.set_goal_position({int(fid):pos})

while True :
    system("clear")
    print(fids)
    print('[d] select servo ,[w] Increase ,[s] Decrease ,[f] set position to a frame ,[p] play few frames')
    pos = float(get_pos()[int(fid)-1])
    u_input = input_cv("change value of servo( {} : {} ) or enter degree ==> {}".format(fid,pos,u_input))
    if (u_input == 'd'): #select servo
        out = input_cv("Inter servo id (current:{}) ==> ".format(fid))
        if (out.isdigit()):
            if (fids.count(int(out))):
                fid = int(out)
    elif (u_input == 'f'):
        s_frame = input_cv("Inter line,frame ==> ").split(',')
        for i in range(2):
            s_frame[i] = int(s_frame[i])-1
        set_pos(frames[s_frame[0]][s_frame[1]])
    elif (u_input == 'p'):
        play_frames(frames,[3])
        while True:
            play_frames(frames,[5,6])
        #play_frames(frames,[31])
        #while True:
        #    play_frames(frames,[38,39,36,37])
    elif (u_input == 'c'):
        out = input_cv("Inter line,frame,id ==> ").split(',')
        for a in range(len(out)):
            out[a] = int(out[a])-1
        pre_value = frames[out[0]][out[1]][out[2]]
        next_value = input_cv("Inter new value({})==> ".format(pre_value))
        frames[out[0]][out[1]][out[2]] = next_value
    elif (u_input == 'l'): 
        save_file(poss_file,frames)
    elif (u_input == 'w'):
        pos += float(2)
        update_pos()
    elif (u_input == 's'):
        pos -= float(2)
        update_pos()
    elif (str(u_input).isdigit()):
        pos = float(u_input)
        update_pos()
        u_input=''
    elif (u_input == 'q'):
        break
dxl.disable_torque(fids)
