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

print("sistem açıldı.")
ses = dinleme()

print(ses)




