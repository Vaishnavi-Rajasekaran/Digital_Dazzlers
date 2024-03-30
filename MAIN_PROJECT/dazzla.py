from ast import main
from multiprocessing.spawn import _main
from msilib import MSIMODIFY_VALIDATE_NEW
from tkinter.tix import MAIN
from tkinter import tix as tk
import requests
import pyautogui
from bs4 import BeautifulSoup
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os,subprocess
import random
import time
import keyboard as kk
import pywhatkit as kit
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

def check_whatsapp(con_name):
    whatsapp_num={
        "vaish":"9385385381","Meena":"9342764784"
    }
    if con_name in whatsapp_num:
        return (whatsapp_num[con_name])
    return "Not Found"

def send_whatsapp_message(contact_name, message):
    contact_number = check_whatsapp(contact_name)
    if contact_number != "Not Found":
        kit.sendwhatmsg_instantly(f"+91{contact_number}", message)
        time.sleep(5)
        pyautogui.press('enter')
    else:
        print("Contact not found")

def send_whatsapp_message_with_number(contact_num, message):
    kit.sendwhatmsg_instantly(f"+91{contact_num}", message)
    time.sleep(5)
    pyautogui.press('enter') 

def remind_exercise():
    speak("It's time to do some exercise. Remember to take care of your health!")

def provide_fitness_tips(health_condition):
    if health_condition == "normal":
        tips = ["Remember to stay hydrated throughout the day.", "Include a variety of fruits and vegetables in your diet.",
                "Try to get at least 30 minutes of exercise every day.", "Make sure to get enough sleep for optimal health."]
        print(tips)
        speak(tips)

    elif health_condition == "diabetic":
        tips = ["Monitor your blood sugar levels regularly.", "Follow a balanced diet with controlled carbohydrate intake.",
                "Engage in regular physical activity to help manage your blood sugar levels.",
                "Consult with your healthcare provider for personalized advice."]
        print(tips)
        speak(tips)
    elif health_condition == "hypertensive":
        tips = ["Limit your sodium intake to help control your blood pressure.", "Engage in regular aerobic exercise such as walking, swimming, or cycling.",
                "Monitor your blood pressure regularly and take medications as prescribed by your doctor.",
                "Practice stress-reduction techniques such as deep breathing or meditation."]
        print(tips)
        speak(tips)
    
    elif health_condition == "Anxiety":
        tips = ["Deep breathing can help calm the nervous system and reduce anxiety symptoms.", "Activities such as progressive muscle relaxation, visualization, or mindfulness meditation can help alleviate anxiety"]
        print(tips)
        speak(tips)

    elif health_condition == "Asthma":
        tips = ["Identify and avoid triggers such as smoke, pollen, dust mites, or pet dander that can worsen asthma symptoms",
                "Use inhalers and other medications as directed by your healthcare provider to manage asthma symptoms effectively"]
        print(tips)
        speak(tips)

    elif health_condition == "Headache":
        tips = ["Dehydration can contribute to headaches, so drink plenty of water throughout the day.",
                "Stress and tension can trigger headaches, so try techniques like deep breathing, meditation, or gentle stretching to relax."]
        print(tips)
        speak(tips)
    else:
        tips = ["Consult with a healthcare professional for personalized health advice.", "Stay informed about your health condition and follow recommended guidelines.",
                "Make healthy lifestyle choices such as eating a balanced diet and staying physically active.",
                "Listen to your body and seek medical attention if you experience any concerning symptoms."]
        print(tips)
        speak(tips)

    #tip = random.choice(tips)
    #speak("Here's a fitness tip for you: " + tip)


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
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
        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            music_dir = 'C:\Audio'
            songs = os.listdir(music_dir)
            rd = random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))
        elif 'exit' in query or 'close' in query:
                speak("Good bye see you soon")
                exit()
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'send' and 'whatsapp' in query:
            nm=query.replace("send","")
            nm=nm.replace("whatsapp","")
            nm=nm.replace("message","")
            nm=nm.replace("to","")
            nm=nm.replace("on","")
            nm=nm.replace(" ",'')
            whatsappNumber=check_whatsapp(nm)
            if whatsappNumber=="Not Found":
                print("This name is not registered on my system. Can you please tell me their number")
                speak("This name is not registered on my system. Can you please tell me their number")
                whatsappNumber=takeCommand()
                print("What do you want me to send?")
                speak("What do you want me to send?")
                message=takeCommand()
                send_whatsapp_message_with_number(whatsappNumber,message)
                speak(f"I have sent the message to {whatsappNumber}!")
                k=True
            else:
                print("What do you want me to send?")
                speak("What do you want me to send?")
                message=takeCommand()
                send_whatsapp_message(whatsappNumber,message)
                speak(f"I have sent the message to {nm}")
        elif "i drink water" in query:
            speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
            while True:
                speak("It's time to drink water. Stay hydrated!")
                time.sleep(7)  #after 7 seconds
                speak("Would you like to stop reminders or continue?")
                inputt = takeCommand().lower()
                if "stop" in inputt:
                    speak("Okay, I'll stop reminding you to drink water.")
                    break
                else:
                    speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
                    time.sleep(7200)
        elif "exercise" in query:
            remind_exercise()
        elif "fitness tips" in query:
            speak("What is your current health condition?")
            health_condition = takeCommand().lower()
            provide_fitness_tips(health_condition)
        elif "emotional wellness" in query:
            speak("Practice mindfulness or meditation to reduce stress and promote mental clarity.",
                "Stay connected with friends and family members for emotional support and social connection.",
                "Seek professional help if you're struggling with your mental health. Therapy and counseling can be beneficial.",
                "Practice self-care activities such as journaling, taking a bath, or going for a walk to recharge emotionally.")
        elif "physical wellness" in query:
            speak("Stay physically active by engaging in regular exercise or physical activity for at least 30 minutes a day.",
                "Eat a balanced diet rich in fruits, vegetables, lean proteins, and whole grains.",
                "Get enough sleep each night, aiming for 7-9 hours for adults.",
                "Stay hydrated by drinking plenty of water throughout the day.")
            
        
        

        
