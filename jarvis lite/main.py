from speak import speak
from listen import listen
from process_command import process_command


speak("hi how can i help you")
while True:
    command=listen()
    process_command(command)
