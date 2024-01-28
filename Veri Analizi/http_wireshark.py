import scapy.all as scapy
from scapy_http import http

def veri_toplama(interface):
    #store depolamaya yarar, prn ise bu verileri ne yapıcaksın
    scapy.sniff(iface=interface,store=False,prn=veri_analiz)

def veri_analiz(paket):
    #paket.show()
    if paket.haslayer(http.HTTPRequest):
        if paket.haslayer(scapy.Raw):
            print(paket[scapy.Raw].load)

veri_toplama("eth0")

