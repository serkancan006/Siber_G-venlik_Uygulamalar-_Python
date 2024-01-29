import socket

baglanti = socket.socket(socket.AF_INET,socket.SOCK)
baglanti.setsockopt(socket.SOL_SOCKET,socke.SO_REUSEADDR,1) 

baglanti.bind(("10.0.2.17",888))
baglanti.listen(0)
print("Dinlemeye Basladi!")


(baglan,adres) = baglanti.accept()

print("baglanti kabul edildi. "+str(adres))

while True:
    giris = input("Komut Gir: ")
    baglan.sendall(giris.encode("utf-8"))
    gelen_veri = baglan.recv(1024).decode("utf-8")
    print(gelen_veri)






