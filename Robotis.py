from time import sleep
from Methods import *

excel_file = "Book1.xlsx"

#dxl.enable_torque(fids)
while True:
    print(get_pos())
    dxl.disable_torque(fids)
    sleep(1)
#    for i in range(1,12):
#        mm=motion(excel_file)[i]
#        set_pos(mm)
#        sleep(4)
