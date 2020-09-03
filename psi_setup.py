from gtts import gTTS
import re
import time
import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import requests
from pygame import mixer
import urllib.request
import urllib.parse
import bs4
import wikipedia
import webbrowser


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

    elif 'youtube' in command:
        talk("Here is Youtube.\n")
        webbrowser.open_new("https://www.youtube.com")

    elif 'github' in command:
        talk("Here is Github.\n")
        webbrowser.open_new("https://github.com/brtymn")

    elif 'metu mail' in command:
        talk("Here is Metu Mail.\n")
        webbrowser.open_new("https://horde.metu.edu.tr/login.php?url=https%3A%2F%2Fhorde.metu.edu.tr%2Fimp%2Fdynamic.php%3Fpage%3Dmailbox&horde_logout_token=WqeTi6ux-c2jmZutU68j0oR#mbox:SU5CT1g")

    elif 'reddit' in command:
        talk("Here is Reddit.\n")
        webbrowser.open_new("https://www.reddit.com/")

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
