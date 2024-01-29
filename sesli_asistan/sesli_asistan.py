import pyaudio
from playsound import playsound
from gtts import gTTS 
import speech_recognition as sr
import os

kayit = sr.Recognizer()

def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""

        try: 
            ses = kayit.recognizer_google(mikrofon, language="tr_TR")
        except sr.UnknowValueError:
            print("Asistan: Anlayamadım.")
        except sr.RequestError:
            print("Asistan: Sistem şu anda çalışmıyor.")

        return ses


def konusma(metin):
    tts = gTTS(text=metin, lang="tr", slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound("konusma.mp3")
    os.remove(ses)


def yanıt(ses):
    if "merhaba" in ses:
        konusma("sanada merhaba dostum")
    if "çıkış" in ses:
        konusma("çıkış yapılıyor.")
        quit()

konusma("Merhaba Serkan.")
print("Başlatıldı...")

while True:

    ses = dinleme()
    if bool(ses)==True:
        print(ses)
        ses = ses.lower()
        yanıt(ses)


