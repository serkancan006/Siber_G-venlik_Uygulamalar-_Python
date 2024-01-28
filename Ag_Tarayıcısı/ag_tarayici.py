import scapy.all as scapy
import optparse

def giris():
    karsvegas = optparse.OptionParser()
    karsvegas.add_option("-i","--ipadres",dest="ip_adresi",help="-i veya --ipadres yazarak yap. örneğin, python tarayici.py -i 10.0.2.1/24")

    (user_giris,arguments) = karsvegas.parse_args()

    if not user_giris.ip_adresi:
        print("La gardas bi ip adresi de mi girmedin! :)")

    return user_giris


def tarayici(ip):
    istek_paket = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    yayin_paket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    paket = yayin_paket/istek_paket
    (asilpaket,gecersizpaket) = scapy.srp(paket,timeout=1)
    asilpaket.summary()

ipadresim = giris()
tarayici(ipadresim)

#netdiscover