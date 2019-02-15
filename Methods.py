import copy
from time import *
import pypot.dynamixel as dynamixel

def play_action(Database_file,action):
    semico = action.split(';') 
    one_time_frame = array_int( semico[0].split(',') )
    loop_frame = array_int( semico[1].split(',') )
    if one_time_frame != ['n']:
        play_frames(Database_file, one_time_frame)
    while  loop_frame != ['n']:
        play_frames(Database_file, loop_frame)

def play_frames(Database_file,selected_frms):
    selected = copy.copy(selected_frms)
    for i in range(len(selected)):
        selected[i] -= 1
    for a in selected:
        for b in Database_file[a]:
            tt = perf_counter() ##
            set_speed(b[18])
            print(perf_counter() - tt) ##
            set_pos(b)
            sleep(b[19]/b[18])

def set_pos(poses):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]] = poses[i]
    dxl.set_goal_position(dicts)

def set_speed(speed):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=speed
    dxl.set_moving_speed(dicts)

def motion_file(addr):
    file = open(addr,'r')
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
