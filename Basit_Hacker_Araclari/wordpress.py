#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")

print("""
WORDPRESS TARAMA aracına hosgeldiniz.

1) Hizli Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yonetici Kullanici Adi Tarama

""")

islemno = raw_input("Islem No Gİriniz: ")

if(islemno == "1"):
    site = raw_input("Site Adresi Gİrin: ")
    os.system("wpscan --url " + site)
elif(islemno=="2"):
    site = raw_input("Site Adresi Gİrin: ")
    os.system("wpscan --url " + site + " --enumerate t")
elif(islemno=="3"):
    site = raw_input("Site Adresi Gİrin: ")
    os.system("wpscan --url " + site + " --enumerate p")
elif(islemno=="4"):
    site = raw_input("Site Adresi Gİrin: ")
    os.system("wpscan --url " + site + " --enumerate u")
else:
    print("Hatalı Secim Yaptiniz. Program Kapatiliyor...")

