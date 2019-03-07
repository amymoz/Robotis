import xmltodict

file = open('soccer.mtnx','r')
data = file.read()
file.close()

xm = xmltodict.parse(data)
xm