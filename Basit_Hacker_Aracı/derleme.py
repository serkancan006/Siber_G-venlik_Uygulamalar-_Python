#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DERLEME ARACI")

print("""
Derleme Aracina Hosgeldiniz :)

bu program .py uzantılı yazılımlarımıcı .pyc yaparak dosyanın içeriğinin görüntülenmicek şekilde olmasını ve compiler olacak şekilde olmasını sağlar.

biz bu .pyc kısmını göndericez.

""")

derle = raw_input("Program Yolunu ve ismini Girin: ")

py_compile.compile(derle)

