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
import home


home.greetMe()
home.speak(' what i can do for you ')

while True:

    query = home.myCommand();
    query = query.lower()
    if 'fever' in query:
        speak('yes sir')
    elif 'weather' in query or 'show me today weather report' in query :
        home.speak('today weather report sir ')
        home.speak('tempreature is {} kelvin '.format(weather.weather()[0]))
        home.speak('and humidity is {} hPa sir' .format(weather.weather()[1]))

    elif 'do maths' in query:
        home.speak('ohk sir .. opening maths part')


    elif 'open youtube' in query:
        home.speak('okay')
        webbrowser.open('www.youtube.com')

    elif 'open google' in query:
        home.speak('okay')
        webbrowser.open('www.google.co.in')

    elif 'open gmail' in query:
        home.speak('okay')
        webbrowser.open('www.gmail.com')

    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ('Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy')
        home.speak(random.choice(stMsgs))

    elif 'email' in query:
        home.speak('Who is the recipient? ')
        recipient = home.myCommand()

        if 'me' in recipient:
            try:
                home.speak('What should I say? ')
                content = home.myCommand()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login("Your_Username", 'Your_Password')
                server.sendmail('Your_Username', "Recipient_Username", content)
                server.close()
                home.speak('Email sent!')

            except:
                home.speak('Sorry Sir! email cant be sent')


    elif 'nothing' in query or 'abort' in query or 'stop' in query:
            home.speak('okay')
            home.speak('Bye Sir, have a good day.')
            sys.exit()

    elif 'hello' in query:
            home.speak('Hello Sir')

    elif 'bye' in query:
            home.speak('Bye Sir, have a good day.')
            sys.exit()

    elif 'play music' in query:
            music_homeder = Your_music_homeder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_homeder + random.choice(music) + '.mp3'
            os.system(random_music)

            home.speak('Okay, here is your music! Enjoy!')



    else:
        query = query
        home.speak('Searching')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                home.speak('WOLFRAM-ALPHA says - ')
                home.speak('Got it')
                home.speak(results)

            except:
                results = wikipedia.summary(query, sentences=4 )
                home.speak('Got it.')
                home.speak('WIKIPEDIA says - ')
                home.speak(results)

        except:
            webbrowser.open('www.google.com')

    home.speak('Anythig else sir!')
