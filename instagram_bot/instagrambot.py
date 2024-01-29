from selenium import webdriver
import time

path = "c:\\Users\efsan\OneDrive\Masaüstü\İnstagrambot\geckodriver.exe"
browser = webdriver.Firefox(executable_path=path)


browser.get("https://www.instagram.com/")
time.sleep(2)

kullanıcı = browser.find_element_by_xpath("chropath_x_path_adı_kullanıcıadı")
sifre = browser.find_element_by_xpath("chropath_x_path_adı_sifre")
kullanıcı.send_keys('battaldenemebot1')
sifre.send_keys('Heycorc123')
browser.find_element_by_xpath('xpath_adı_giris_yap').click()

time.sleep(10)

browser.get('https://www.instagram.com/battaldenemebot1/')
time.sleep(1)
browser.find_element_by_xpath('ayalar_xpath').click()
browser.find_element_by_xpath('cikis_yap_xpath').click()




