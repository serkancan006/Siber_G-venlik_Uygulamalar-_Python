#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC DEGISTIRME")

print("""
Mac Degistirme aracına hosgeldiniz.

1) Mac ADresi Random Belirle
2) Mac Adresi Elle Belirleme
3) Mac ADresi Orjinale Döndür.

eth0 için yapılmıştır.
""")

islemno = raw_input("Islem No Giriniz: ")

if(islemno=="1"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mYeni Mac Adresi Elle Belirlendi.")  #\033 gibi olan kısım renk kodu ile ilgili.
elif(islemno=="2"):
    macadres = raw_input("Yeni Mac Adresi Gİrin: ")
    os.system("ifconfig eth0 down")
    os.system("macchanger --mac "+macadres+" eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mYeni Mac Adresi Elle Belirlendi.")
elif(islemno=="3"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mMac Orjinale Dondu.")
else:
    print("Hatalı Tuslama yaptiniz yeniden baslatiliyor...")
    os.system("python mac.py")


