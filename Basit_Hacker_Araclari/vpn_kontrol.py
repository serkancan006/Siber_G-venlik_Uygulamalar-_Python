#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN KONTROL")

print("""
VPN Kontrol aracına hosgeldiniz.

""")

hedefip = raw_input("Hedef Ip Girin: ")
os.system("ike-scan " + hedefip)
