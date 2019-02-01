poss_file = "/media/Game/Professional/Project/GitArch/Robotis/poss.txt"
poss_file2 = "/media/Game/Professional/Project/GitArch/Robotis/poss2.txt"

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
frames = motion_file(poss_file,0)
save_file(poss_file2,frames)
