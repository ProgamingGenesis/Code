import speech_recognition
import pyttsx3
from playsound import playsound
recognizer = speech_recognition.Recognizer()

while True:

    try:
        
        with speech_recognition.Microphone() as mic:
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

            if text == "bye":
                break
            
            if text == "bing bong":
                playsound('fuckyalife.mp3')


    except:

        recognizer = speech_recognition.Recognizer()
        print("didn't quite catch that")
