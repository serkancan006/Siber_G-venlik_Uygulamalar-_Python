from selenium import webdriver
import time

print("""
Instagram Bot
Hos Geldiniz!

1) Takip

2) Begeni

3) Yorum

""")
secim = input("Giriniz: ")
sira = 1
takipkontrol = 0
begenikontrol = 0
yorumkontrol = 0
if secim=="1":
    ad = input("Kullanıcı adı giriniz: ")
    takipkontrol = 1
elif secim=="2":
    link = input("begenilecek gonderi linkini giriniz: ")
    begenikontrol = 1
elif secim=="3":
    link = input("yorum atılacak gönderi linkini giriniz: ")
    yorum = input("atılacak yorumu giriniz: ")
    yorumkontrol = 1


path = "c:\\Users\efsan\OneDrive\Masaüstü\İnstagrambot\geckodriver.exe"
browser = webdriver.Firefox(executable_path=path)

while True:
    browser.get("https://www.instagram.com/")
    time.sleep(2)

    kullanıcı = browser.find_element_by_xpath("chropath_x_path_adı_kullanıcıadı")
    sifre = browser.find_element_by_xpath("chropath_x_path_adı_sifre")
    kullanıcı.send_keys('battaldenemebot'+str(sira))
    sifre.send_keys('Heycorc123')
    browser.find_element_by_xpath('xpath_adı_giris_yap').click()
    time.sleep(2)
    if takipkontrol==1:
        browser.get("https://www.intagram.com/"+ad)
        time.sleep(2)
        browser.find_element_by_xpath("xpath_takip_et").click()
    if takipkontrol==1:
        browser.get(link)
        time.sleep(2)
        browser.find_element_by_xpath("xpath_begeni_button").click()
    if yorumkontrol==1:
        browser.get(link)
        time.sleep(2)
        browser.find_element_by_xpath("yorum_yap_icon_xpath").click()
        time.sleep(1)
        browser.find_element_by_xpath("yorum_yap_formu_xpath").send_keys(yorum)
        time.sleep(1)
        browser.find_element_by_xpath("yorum_paylas_xpath").click()

    time.sleep(3)

    browser.get('https://www.instagram.com/battaldenemebot'+str(sira))
    time.sleep(1)
    browser.find_element_by_xpath('ayalar_xpath').click()
    browser.find_element_by_xpath('cikis_yap_xpath').click()
    time.sleep(1)
    sira += 1
    if sira==5:
        break

browser.close()



