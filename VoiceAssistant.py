# Shree Ganeshay Namah
# Vaak (Emily)
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import datetime
import requests
import speech_recognition as sr
import smtplib
import wikipedia
import pyjokes
import wolframalpha
import random
import re
import pywhatkit as kit
import os
import pyaudio
import pvporcupine
import struct
import calendar
import threading
# import tkinter as tk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


"""
Speak() function handls the main functionality of voice assistant, that is 
voice. It gives voice to all the result of commands. It uses pyttsx3 module to
assign voices.
"""


def speak(audio):
    global engine
    engine.say(audio)
    engine.runAndWait()


"""
WhishMe() function wishes you according to time.
"""


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # we can also write it as hour>=0 and hour<1
    if 0 <= hour < 12:
        print("Good Morning")
        speak("Good Morning")
        # hour>=12 and hour<18
    elif 12 <= hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")

    print("Hello, I am Emily, What can I do for you ?")
    speak("Hello, I am Emily, What can I do for you ?")


"""
TakeCommand() function takes commands from the user and returns string output
"""
query = " "

def TakeCommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(1.5)
        print("Listening...")
        r.pause_threshold = 2.5
        r.energy_threshold = 100
        audio = r.listen(source, 0, 8)

    try:
        # print("Listening...")
        query = r.recognize_google(audio, language='en-in')
        print("Recognizing...")
        print(f"User said: \n{query}\n")

    except Exception as e:
        print(e)
        print("Sorry, I didn't catch that \n Can you say that again...")
        speak("Sorry, I didn't catch that \n Can you say that again...")
        return "None"
    return query



"""
To give task to our voice assistant
"""


def TaskExecution():

    wishMe()
    while True:      # to give continuous commands after detected wake up word
        commands = TakeCommand().lower()
