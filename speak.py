import pyttsx3

# Create the engine only once
engine = pyttsx3.init()

# Set speaking speed
engine.setProperty("rate", 150)

# Set volume
engine.setProperty("volume", 1.0)


def speak(text):
    if text and text != "Word not found":
        engine.say(text)
        engine.runAndWait()