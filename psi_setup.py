from gtts import gTTS
from pygame import mixer
import sys
import time

from psi_greet import Greet

Greet()

def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()


def userCommand():

    command = input("---->")

    return command

import random

def reactPsi(command):

    errors=[
        "I don\'t know what you mean.",
        "Excuse me?",
        "Can you repeat it please?",
    ]

    if 'Hello' in command:
        talk('Hello! I am Psi. How can I help you?')
    elif 'Exit' in command:
        talk("Psi deactivating now.")
        time.sleep(4)
        sys.exit()

    else:
        error = random.choice(errors)
        talk(error)


talk('Hey, Psi is ready! What do you need?')


while True:
    reactPsi(userCommand())
