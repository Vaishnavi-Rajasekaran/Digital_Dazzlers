import os,subprocess
import random
import pyttsx3
import datetime
import speech_recognition as sr



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

def music():
    music_dir = 'C:\Audio'
    songs = os.listdir(music_dir)
    rd = random.choice(songs) 
    os.startfile(os.path.join(music_dir, rd))

def audiobooks():
    music_dir = 'C:\Audio_books'
    songs = os.listdir(music_dir)
    rd = random.choice(songs) 
    os.startfile(os.path.join(music_dir, rd))

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "play music" in query:
            music()
        elif "play books" in query:
            audiobooks()