import xlrd
import pypot.dynamixel as dynamixel
#Start Dynamixel
port = dynamixel.get_available_ports()[0]
dxl = dynamixel.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))

def set_pos(poses):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=(poses[i]-512)*0.29
    dxl.set_goal_position(dicts)

def get_pos():
    return dxl.get_present_position(tuple(fids)) #Tuple

def motion(addr):
    WorkBook = xlrd.open_workbook(addr)
    sheet = WorkBook.sheet_by_index(0)
    amotion = []
    angles = []
    for a in range(sheet.nrows):
        for b in range(sheet.ncols):
            meghdr = sheet.cell_value(a, b)
            angles.append(int(meghdr))
        amotion.append(angles)
        angles = []
    return amotion
