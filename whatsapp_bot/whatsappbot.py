from selenium import webdriver
import smtplib
import time

path = 'C:\\path/geckodriver.exe'

browser = webriver.Firefox(executeable_path=path)

#browser.get("https://www.friv.com")
browser.get("https://www.web.whatsapp")

time.sleep(5)
browser.find_element_by_xpath("eskry ile bulunan whatsapp kişisinin adının oldugu buton").click()

def mailgonder(mesaj):
    sahip='wpbothacker@gmail.com'
    gonderilecekhesap="konya.siberkurs@gmail.com"
    giris="wpbothacker@gmaik.com"
    sifre="20202Hacker"

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(giris,sifre)
    server.sendmail(sahip,gonderilecekhesap,mesaj)
    server.quit()


kontrol=True
kontrol2=True
kontrol3=False
baslangic = 0
while True:
    try:
        #browser.find_element_by_xpath("eskry").click()    #eskry ile buldugumuz selectorun isimini yazıyoruz.
        browser.find_element_by_xpath("eskry_whatsapweb_çevrimiçi _butonu")
        if kontrol==True:
            msg2="çevrimiçi!"
            mailgonder(msg2)
            baslangic = time.time()
            kontrol=False
            kontrol2=True
            kontrol3=True
    except:
        kontrol=True
        if kontrol2=True:
            msg="çevrimdışı!"
            mailgonder(msg)
            if kontrol3 == True:
                bitis=time.time() - baslangic
                mailgonder(str(bitis))
                baslangic=time.time()
            kontrol2=False





