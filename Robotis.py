from time import sleep
from Methods import *

excel_file = "Book1.xlsx"
releases=[17,18,9,10,1,2,3,4,5,6]
dxl.enable_torque(fids)
mm=motion(excel_file)[1]
res = (-81.67, 81.09, -68.48, 55, -14.52, 13.64, -46.19, 44.72, -3.37, 15, -46.77, 55.28, -73.75, 90.76, 36.51, -46.19, 20, 9.24)
set_pos(res)
while True:
    print(get_pos())
    sleep(1)
#    dxl.disable_torque(fids)
#    for i in range(1,12):
#        mm=motion(excel_file)[i]
#        set_pos(mm)
#        sleep(4)
