import pyttsx3
engine=pyttsx3.init()

def speak(text):
    engine.setProperty('rate',120)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


