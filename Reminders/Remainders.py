import pyttsx3
import speech_recognition as sr
import time
import datetime
import wikipedia
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak ("Good evening")
    speak("Hello i am  your Dazzla, what can i do for you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        print("Say that again please...")
        return"None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if "weather" in query:
          speak("Sir, which city's weather report you want")
          cty=takeCommand().lower()
          search=f"Weather in {cty}"
          url=f"https://www.google.com/search?&q={search}"
          r=requests.get(url)
          s=BeautifulSoup(r.text,"html.parser")
          update=s.find('div',class_="BNeawe").text
          print(update)
          speak(update)
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "i drink water" in query:
            speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
            while True:
                speak("It's time to drink water. Stay hydrated!")
                time.sleep(7200)  # 2 hours in seconds
                speak("Would you like to stop reminders or continue?")
        elif "stop" in query:
            speak("Okay, I'll stop reminding you to drink water.")
            break
        else:
            speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
            time.sleep(7200)