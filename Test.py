# Import the necessary libraries
import speech_recognition as sr
from gtts import gTTS
import os

# Set up the speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# Create a function to listen for and respond to voice commands
def listen_and_respond():
    # Listen for voice input
    with mic as source:
        audio = r.listen(source)
    try:
        # Convert the speech to text
        text = r.recognize_google(audio)
        print(text)

        # Respond to the command
        if "hello" in text:
            response = "Hello, how can I help you?"
        else:
            response = "Sorry, I didn't understand that command."

        # Convert the response to speech
        tts = gTTS(response, lang="en")
        tts.save("response.mp3")

        # Play the response
        os.system("start response.mp3")
    except sr.UnknownValueError:
        # If the speech could not be recognized, do nothing
        pass

# Run the function indefinitely
while True:
    listen_and_respond()
