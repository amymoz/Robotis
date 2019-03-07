#!/usr/bin/python3
from copy import copy
from time import sleep
import pypot.dynamixel as dynamixel
from os import system
import threading

actions = {
    'Soccer_Left' : '23;n;100,15',
    'Soccer_Right' : '24;n;100,15',
    'Soccer_Forward_wow' : 'n;9,10;300,20',#'9,s8,10,s7'
    'Soccer_Balance' : '2;n',
#    'Soccer_Forward' : '4;6,5;100,10',
    'Soccer_Forward' : 'n;6,5;97,9',#90,9
    'Soccer_Forward_Right' : 'n;11;200,20',#200
    'Soccer_Forward_Left' : 'n;12;200,20',
    'Soccer_Backward' : '14;16,15;150,15',
    'Soccer_Turn_Right' : '21;n',
    'Soccer_Turn_Left' : '22;n',
    'Soccer_Shoot_Right' : '31,32;n',
    'Soccer_Shoot_Left' : '33,34;n',
    'Soccer_Pass_Right' : '39;n;250,25',
    'Soccer_Pass_Left' : '40;n;400,40',
    'TypeA_Forward' : '32,33;38,39,36,37;100,2',
    'TypeA_Backward' : '44,45;50,51,48,49',
    'TypeA_Forward_Left' : '104,105;110,111,108,109',
    'TypeA_Forward_Right' : '116,117;122,123,120,121',
    'TypeA_Standup_Front' : '27;n',
    'TypeA_Standup_Back' : '28;n'
}

def motion_file(file_address):
    file = open(file_address,'r')
    data = file.read()
    file.close()
    amotion = []
    frms = []
    frm = []
    for a in data.split('\n'):
        str_frms = str(a).split(';')
        for b in range(1,len(str_frms)):
            str_frm = str(str_frms[b]).split(',')
            for c in range(len(str_frm)):
                frm.append(float(str_frm[c]))
            frms.append(frm)
            frm = []
        amotion.append(frms)
        frms = []
    return amotion

DataBase = {'Soccer':motion_file('Soccer.db'),
             'TypeA':motion_file('TypeA.db')}

def play_action(action,nump = 1):
    print(action)
    Database_file = DataBase[action.split('_')[0]]
    action = actions[action]
    action = action.split(';')
    one_time_frame =  action[0].split(',')
    loop_frame = action[1].split(',')
    duration = []
    if (len(action) == 3):
        duration = array_int(action[2].split(','))
    
    if one_time_frame != ['n']:
        play_lines(Database_file, array_int(one_time_frame), duration=duration)
    
    if loop_frame != ['n']:
        for i in range(nump):
            play_lines(Database_file, array_int(loop_frame), duration=duration)

def play_lines(Database_file,line_array,duration=[]):
    lines = copy(line_array)
    for i in range(len(lines)):
        lines[i] -= 1
    for a in lines:
        for b in Database_file[a]:
            if (len(duration)>0):
                set_speed(duration[0])
            else:
                set_speed(b[18])
            set_position(b)
            if (len(duration)>0):
                sleep(duration[1]/duration[0])
            else:
                sleep(b[19]/b[18])

def set_position(positions):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]] = positions[i]
    dicts[11] -= 5
    dicts[12] += 5
    dxl.set_goal_position(dicts)

def set_speed(speed):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=speed
    dxl.set_moving_speed(dicts)

def array_int(out):
    for a in range(len(out)):
        out[a] = int(out[a])
    return out

port = dynamixel.get_available_ports()[0]
dxl = dynamixel.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))
dxl.enable_torque(fids)

global robo_play
robo_play = 'Soccer_Balance'
def play_live():
    while robo_play != False:
        play_action(robo_play)

if __name__ == "__main__":
    while True:
        system('clear')
        print(fids)
        output_str = ''
        for a in range(len(actions.keys())):
            output_str += str(a+1) +' ==> ' + list(actions.keys())[a] + '\n'
        output_str += 'Enter number of action to run ==> '
        act = str(list(actions.keys())[int(input(output_str))-1])
        play_action(act)
#else:
#    threading.Thread(target=play_live).start()
