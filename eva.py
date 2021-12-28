import speech_recognition
from gtts import gTTS
import os
import pyttsx3
from playsound import playsound
recognizer = speech_recognition.Recognizer()

def speak(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("EVA_AUDIO.mp3")
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("EVA_AUDIO.mp3")
    playsound('EVA_AUDIO.mp3')
    
speak("Hello I am Eva, at your service")

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized {text}")
            
            if "bye" in text:
                break

            if "calculate" in text:

                if "+" in text:
                    i = 0
                    nums = []
                    while i != 9:
                       answ = text.find(str(i))
                       if answ != -1:
                         nums.append(i)
                       
                       i = i + 1
                    print("The answer is", nums[0] + nums[1] )
                       
    except:
        recognizer = speech_recognition.Recognizer()
        print("Didn't quite catch that")