import pyttsx3
import speech_recognition as sr
import webbrowser
import os
def speak(text):
    engine = pyttsx3.init() # object creation
    engine.setProperty('rate',125)
    engine.setProperty('volume',1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen():
    speak("hi,i am your personal assistant")
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
        

    try:
        command = r.recognize_google(audio)
        print(f"You said - {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that.")
    except sr.RequestError as e:
        speak("Request failed; please check your internet connection.")
        print(f"RequestError: {e}")
    




def command_process(command):
    
    if 'youtube' in command:
        speak("openning youtube...")
        webbrowser.open("https://youtube.com")
    
    elif 'how are you' in command:
        speak("i am good")

    elif 'notepad' in command:
        speak("i am trying to open notepad")
        try:
            os.system("Notepad")
        except:
            speak("i didnt found notepad")
        



