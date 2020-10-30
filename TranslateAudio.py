import numpy as np
import threading
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def voiceREC():
    r = sr.Recognizer()
    mic = sr.Microphone()
    while(True):

        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:   
            dialogue = r.recognize_google(audio)
            dialogue = str(dialogue)
            print(dialogue)
            ToLanguage(dialogue)
        except:
            pass
         
def ToLanguage(text):
    translator.detect(text)
    LanguageInputDetected = translator.detect(text)
    LanguageInputDetected = str(LanguageInputDetected)
    
    if (LanguageInputDetected.find("lang=en") !=-1):
        #if input is english 
        destination = "es"  # go to spanish
        
        
    if(LanguageInputDetected.find("lang=en") ==-1):
        #if input is not english
        destination = "en" # go to english
        
        
    translations = translator.translate([text], dest=destination)
    for translation in translations:
         print(translation.text)
         SpeechSynth(translation.text)
         
def SpeechSynth(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
      print("Speechsynth error")

if __name__ == "__main__":
    translator = Translator()
    voiceREC = threading.Thread(target=voiceREC) 
    voiceREC.start()
    
   
