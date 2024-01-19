import cowsay
import pyttsx3
engine = pyttsx3
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()

## text into voice