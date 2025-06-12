import speech_recognition as sr
from speak import speak  # assuming this is your custom TTS function

def listen():
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
