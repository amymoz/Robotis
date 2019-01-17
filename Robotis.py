from time import sleep
from Methods import *

excel_file = "Book1.xlsx"

#dxl.enable_torque(fids)
mm=motion(excel_file)[1]
set_pos(mm)

while True:
    print(get_pos())
    sleep(1)
    dxl.disable_torque(fids)
#    for i in range(1,12):
#        mm=motion(excel_file)[i]
#        set_pos(mm)
#        sleep(4)
