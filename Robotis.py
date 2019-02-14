#!/usr/bin/python3
from os import system
from time import sleep
import cv2

from Methods import *

DataBase_TypeA = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/TypeA.db')
DataBase_Soccer = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/Soccer.db')

dxl.enable_torque(fids)

actions= {
    'TypeA_f_s_l' : '31;38,39,36,37:120,2.5',
    'Soccer_Left_Turn' : '22;n:100,15',
    'Soccer_Right_Turn' : '21;n:100,15',
    'Soccer_Run' : '3;5,6:120,10',
    'TypeA_Backward' : '44,45;50,51,48,49:100,3',
    'TypeA_Standup_Front' : '27;n:130,230',
    'Soccer_28' : '30;n:130,230',
    'TypeA_18' : '18;n:100,150',
    'Soccer_Shoot_Right' : '31,32;n:500,20'
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
