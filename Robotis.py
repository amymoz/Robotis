#!/usr/bin/python3
from os import system
from time import sleep
import cv2
from Methods import *

DataBase_TypeA = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/TypeA.db')
DataBase_Soccer = motion_file('/media/root/Game/Professional/Project/GitArch/Robotis/Soccer.db')
frames = DataBase_TypeA

dxl.enable_torque(fids)

set_speed(100)

actions= {
    'TypeA_f_s_l' : '31;38,39,36,37'
    'TypeA_Rotation' : '80,81;86,87,84,85'
    'Soccer_Run' : '3;5,6'
}

while True :
    system('clear')

    output_str = ''
    for a in range(len(actions.keys())):
        output_str += str(a+1) +' ==> ' + actions.keys()[a] + '\n'
    output_str += 'Enter number of action to run ==> '
    
    play = actions[actions.keys()[int(input(output_str))-1]]

    play_frames(frames,play.split(';')[0].split(',')) 
    while True:
        play_frames(frames,play.split(';')[1].split(','))

dxl.disable_torque(fids)
