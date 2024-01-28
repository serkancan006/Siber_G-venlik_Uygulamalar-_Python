import subprocess
import optparse
import re

def giris():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface degistirme :) ")
    parse.add_option("-m","--mac",dest="mac_adress",help="Yeni mac adres")

    return parse.parse_args()

def mac(inter,mac_adres):
    #ifconfig --help
    subprocess.call([["ifconfig",inter,"down"]])
    subprocess.call(["inconfig",inter,"hw","ether",mac_adres])
    subprocess.call(["ifconfig",inter,"up"])

def kontrol(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    Ymac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if Ymac:
        return Ymac.group(0)
    else:
        return None


print("mac degistirici baslatildi.")
(userInput,arguments) = giris()
mac(userInput.interface, userInput.mac_adress)
Emac = kontrol(userInput.interface)

if Emac == userInput.mac_adress:
    print("Basarili!")
else:
    print("Basarisiz!")    



#python hacker.py -i eth0 --mac 00:11:33:22:55:44
#regex101.com   \d\d:   \w\w:\w\w:\w\w:
