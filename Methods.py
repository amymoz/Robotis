import copy
from time import *
import pypot.dynamixel as dynamixel

def play_action(Database_file,action):
    one_time_frame = action.split(':')[0].split(';')[0].split(',')
    loop_frame = action.split(':')[0].split(';')[1].split(',')
    speed = float(action.split(':')[1].split(',')[0])
    duration = float(action.split(':')[1].split(',')[1]) / speed
    set_speed(speed)
    if one_time_frame != ['n']:
        play_frames(Database_file,array_int(one_time_frame),duration=duration)
    if loop_frame != ['n']:
        while True:
            play_frames(Database_file,array_int(loop_frame),duration=duration)

def play_frames(Database_file,selected_frms,duration=0.0):
    slected = copy.copy(selected_frms)
    for i in range(len(slected)):
        slected[i] -= 1
    for a in slected:
        for b in Database_file[a]:
            set_pos(b,wait=True,duration=duration)

def set_pos(poses, wait=False, duration=0.0):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=poses[i]
    dxl.set_goal_position(dicts)
    if wait:
        sleep(duration)

def set_speed(sped):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=sped
    dxl.set_moving_speed(dicts)

def array_int(out):
    for a in range(len(out)):
        out[a] = int(out[a])
    return out

def array_float(out):
    for a in range(len(out)):
        out[a] = float(out[a])
    return out

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
                frm.append(str_frm[c])
            frms.append(frm)
            frm = []
        amotion.append(frms)
        frms = []
    return amotion

#Start Dynamixel
port = dynamixel.get_available_ports()[0]
dxl = dynamixel.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))
