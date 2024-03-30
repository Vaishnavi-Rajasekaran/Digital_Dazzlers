import speech_recognition as sr
import datetime
import pyttsx3
from twilio.rest import Client
import time
import keyboard as kk
import pywhatkit as kit
import pyautogui

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

account_sid = 'AC7b5e61ad2b4c0d1edf99e544a7413862'
auth_token = '217e5d24c2c317a14403881095a9128a'
client = Client(account_sid, auth_token)

def make_phone_call(to_number, from_number, message):
    client.calls.create(
        twiml=f'<Response><Say>{message}</Say></Response>',
        to=to_number,
        from_=from_number
    )

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
    

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "phone call" in query:
            make_phone_call('+918072442952','+919500236467', 'Hello, Good Morning I am dazzla I am here to inform to call the user ')

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

