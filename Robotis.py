#!/usr/bin/python3
from os import system
from time import sleep
import cv2

from Methods import *

DataBase_TypeA = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/TypeA.db')
DataBase_Soccer = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/Soccer.db')

dxl.enable_torque(fids)

#set_speed(150)

actions= {
    'TypeA_f_s_l' : '31;38,39,36,37:100,0.02',
    'TypeA_Rotation' : '80,81;86,87,84,85',
    'Soccer_Run' : '3;5,6'
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
