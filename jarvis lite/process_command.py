import datetime
import webbrowser
import wikipedia
import pywhatkit
from speak import speak


def process_command(command):
    if 'date' in command:
        date=datetime.datetime.now().strftime("%I:%M %p")
        speak(f'the time is {date}')


    elif 'youtube' in command:
        try:
            speak("opening youtube")
            webbrowser.open("https://youtube.com")

        except:
            speak("check your internet connection")

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "who is" or "what is " in command:
        summary=wikipedia.summary(command,1)
        speak(summary)


    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I can't do that yet.")

