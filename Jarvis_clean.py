#!pip install pyttsx3
#!pip install speechRecognition
#!pip install wikipedia
#!pip install pyaudio
#!pip install TTS==0.14.3
#!pip install gpt4free

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import requests
from gpt4free import usesless

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if datetime.datetime.now().month == 9 and datetime.datetime.now().day == 5:
        speak("Happy Birthday Anish")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

#Get weather using weather api

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=41.763889&lon=-88.290001&appid=API_KEY&units=imperial"
    response = requests.get(url).json()
    return response['main']['temp']

#A GPT API which returns response when given the prompt

def get_gpt(prompt):
    message_id = ""
    i = 0
    while i <= 0:
        req = usesless.Completion.create(prompt=prompt, parentMessageId=message_id)
        message_id = req["id"]
        return req['text']
    
 # Activating Jarvis   

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "path"
            os.startfile(codePath)

        elif 'bye' in query:
            speak("Bye")
            break

        elif 'email to anish' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ani.bellamkonda@Gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend anish bhai. I am not able to send this email")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'when is my birthday' in query:
            speak("Bhai your birthday is on September 5th")

        elif 'what is the weather' in query:
            speak(f"The weather is {get_weather()} Fahrenheit")

        elif 'i have a question' in query:
            q = input("What is your question?")
            speak(get_gpt(q))
