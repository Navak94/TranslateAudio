import numpy as np
import threading
import speech_recognition as sr

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
            
        except:
          print("Google Speech recognition failed")
         
      
if __name__ == "__main__":
    voiceREC = threading.Thread(target=voiceREC) 
    voiceREC.start()
    
   

