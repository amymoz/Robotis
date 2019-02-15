#!/usr/bin/python3
from os import system
from time import *
import cv2
from Methods import *

DataBase_TypeA = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/TypeA2.db')
DataBase_Soccer = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/Soccer2.db')

dxl.enable_torque(fids)

#'Soccer_Run2' : 'n;9,10:120,10',
#'Soccer_Run3' : '3;5,6:120,10',
#'TypeA_Forward' : '31;38,39,36,37:120,2.5',
#'TypeA_Backward' : '44,45;50,51,48,49:100,3',

actions= {
    'Soccer_Forward' : '4;6,5',
    'Soccer_Backward' : '14;16,15',
    'Soccer_Right_Turn' : '21;n',
    'Soccer_Left_Turn' : '22;n',
    'Soccer_Shoot_Right' : '31,32;n',
    'Soccer_Pass' : '39;n',
    'TypeA_Standup_Front' : '27;n'
}

while True :
    system('clear')

    output_str = ''
    for a in range(len(actions.keys())):
        output_str += str(a+1) +' ==> ' + list(actions.keys())[a] + '\n'
    output_str += 'Enter number of action to run ==> '
    act = str(list(actions.keys())[int(input(output_str))-1])
    play = actions[act]
    
    if act.startswith('TypeA'):
        play_action(DataBase_TypeA,play)
    elif act.startswith('Soccer'):
        play_action(DataBase_Soccer,play)

dxl.disable_torque(fids)
