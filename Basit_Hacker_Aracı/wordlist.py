#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDLİST OLUSTURMA")

print("""
WORDLİST OLUSTURMA aracına hosgeldiniz.

""")

minimum = raw_input("Minimum Karakter Sayisini Girin: ")
maximum = raw_input("maximum Karakter Sayisini Girin: ")
karkaterler = raw_input("Istediğiniz karakterleri Girin: ")

os.system("crunch " + minimum + " " + maximum + " " + Karakter )

print("basariyla tamamlandi...")

#kayit yeri kısmı yapabilirsin.