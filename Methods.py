import threading
from time import *
import xlrd
import cv2
from os import system
import pypot.dynamixel as dynamixel

class hom:
    prev_pos = [0]
    speed = 0

def prt(st,end='\n'):
    system("printf \"{0}\"".format(st+end))

def array_int(out):
    for a in range(len(out)):
        out[a] = float(out[a])
    return out

def play_action(Database_file,action):
    play_frames(Database_file,action.split(';')[0].split(','))
    while True:
        play_frames(Database_file,action.split(';')[1].split(','))

def set_speed(sped):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=sped
    hom.speed = sped
    dxl.set_moving_speed(dicts)

def get_speed():
    return dxl.get_moving_speed(fids)

def get_pos():
    return dxl.get_present_position(tuple(fids)) #Tuple

def set_pos(poses, wait=True):
    if len(hom.prev_pos) < 2:
        hom.prev_pos = poses
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=poses[i]
    duration = 0.0
    if wait:
        dp = max_position(hom.prev_pos,poses)
        duration = (10 / float(hom.speed)) if hom.speed > 0 else 0
    dxl.set_goal_position(dicts)
    if wait:
        sleep(duration)
    
def max_position(present_array, next_array):
    dp = 0.0
    present_array = array_int(present_array)
    next_array = array_int(next_array)
    for a in range(len(present_array)):
        dpp = abs( present_array[a] - next_array[a])
        if dpp > dp :
            dp = dpp
    return dp

def play_frames(file_frms,selected_frms):
    for i in range(len(selected_frms)):
        selected_frms[i] -= 1
    for a in selected_frms:
        for b in file_frms[a]:
            set_pos(b)

def motion_excel(addr):
    WorkBook = xlrd.open_workbook(addr)
    sheet = WorkBook.sheet_by_index(0)
    amotion = []
    angles = []
    for a in range(sheet.nrows):
        for b in range(sheet.ncols):
            meghdr = sheet.cell_value(a, b)
            angles.append(meghdr)
        amotion.append(angles)
        angles = []
    return amotion

def motion_file(addr,starti=1):
    file = open(addr,'r')
    data = file.read()
    file.close()
    amotion = []
    frms = []
    frm = []
    for a in data.split('\n'):
        str_frms = str(a).split(';')
        for b in range(starti,len(str_frms)):
            str_frm = str(str_frms[b]).split(',')
            for c in range(len(str_frm)):
                frm.append(str_frm[c])
            frms.append(frm)
            frm = []
        amotion.append(frms)
        frms = []
    return amotion

def save_file(addr,arr_file):
    file = open(addr,'w+')
    frm=''
    frms=''
    for a in arr_file:
        for b in a:
            ss = str(b).replace('[','').replace(']','').replace(' ','').replace('\'','') + ';'
            frm += ss
        frms += frm[:len(frm)-1]+'\n'
        frm = ''
    frms = frms[:len(frms)-1]
    file.write(frms)
    file.close()

def compare_me(first_arr,second_arr,compare_ratio):
    for a in range(len(first_arr)):
        minus = float(first_arr[a]) - float(second_arr[a])
        if minus < 0 :
            minus = -1 * minus
        if minus > compare_ratio :
            return False
    return True

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
            if (instr == ''):
                return 'enter'
            else:
                return str(instr)

#Start Dynamixel
port = dynamixel.get_available_ports()[0]
dxl = dynamixel.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))
