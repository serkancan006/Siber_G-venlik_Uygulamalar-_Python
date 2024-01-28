#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Guvenlik DUvarı Tespiti")

print("""
Guvenlik DUvarı Tespit etme aracına hosgeldiniz.

""")

site = raw_input("Site Adresini Giriniz: ")
os.system("wafw00f " + site)


