#!/usr/bin/python3
from os import system
import cv2
cv2.namedWindow('window')
def prt(st,end='\n'):
    system("printf \"{0}\"".format(st+end))

def input_cv(outstr):
    instr=''
    while True :
        prt("\033[2K\033[0G"+outstr+instr,end='')
        key=cv2.waitKeyEx(0)
        if ((key < 58 and key > 47) or (key == 39) or (key < 48 and key > 41) or (key == 61)):
            instr += chr(int(key))
        elif (key > 96 and key < 123):
            print('')
            return chr(int(key))
        elif (key == 8):
            instr = instr[:len(instr)-1]
        elif (key == 13):
            print('')
            return instr
