import numpy as nm #pip install numpy
import math
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import weather
import home
import re #pip install regex
home.speak('evironment is creted sir..')
query=home.myCommand():
query=query.lower()
if 'ohk' in query:
	home.speak('ohk  sir')


def myCommand_math():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query_math = r.recognize_google(audio, language='en-in')
        print('User: ' + query_math + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query_math = str(input('Command: '))

    return query_math


while True:
	query_math = home.myCommand_math();
    query_math= query_math.lower()
	if ''

def user_gp(n): # this function creates the loop for user input
	for in range (n):
		input_1=int(input())

def summation(x):
	result=nm.sum(x)
	return result
