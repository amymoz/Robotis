import copy
from time import *
import pypot.dynamixel as dynamixel

actions = {
    'Soccer_Forward' : '4;6,5',
    'Soccer_Backward' : '14;16,15',
    'Soccer_Turn_Right' : '21;n',
    'Soccer_Turn_Left' : '22;n',
    'Soccer_Shoot_Right' : '31,32;n',
    'Soccer_Pass_Right' : '39;n',
    'TypeA_Standup_Front' : '27;n',
    'TypeA_Forward' : '31;38,39,36,37'
    #'TypeA_Backward' : '44,45;50,51,48,49',
}

def play_action(Database_file,action):
    semico = action.split(';') 
    one_time_frame =  semico[0].split(',')
    loop_frame = semico[1].split(',')
    if one_time_frame != ['n']:
        play_lines(Database_file, array_int(one_time_frame))
    while  loop_frame != ['n']:
        play_lines(Database_file, array_int( loop_frame))

def play_lines(Database_file,line_array):
    lines = copy.copy(line_array)
    for i in range(len(lines)):
        lines[i] -= 1
    for a in lines:
        for b in Database_file[a]:
            set_speed(b[18])
            set_position(b)
            sleep(b[19]/b[18])

def set_position(positions):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]] = positions[i]
    dxl.set_goal_position(dicts)

def set_speed(speed):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=speed
    dxl.set_moving_speed(dicts)

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

def array_int(out):
    for a in range(len(out)):
        out[a] = int(out[a])
    return out

#Start Dynamixel
port = dynamixel.get_available_ports()[0]
dxl = dynamixel.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))
