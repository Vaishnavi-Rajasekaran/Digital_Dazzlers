import pyttsx3
import speech_recognition as sr
import time
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print("You said: " + said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def main():
    while True:
        speak("How can I help you?")
        query = get_audio()

        if "i drink water" in query:
            speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
            while True:
                speak("It's time to drink water. Stay hydrated!")
                time.sleep(7200)  # 2 hours in seconds
                speak("Would you like to stop reminders or continue?")
                query = get_audio()
                if "stop" in query:
                    break
        elif "stop" in query:
            speak("Okay, I'll stop reminding you to drink water.")
            break
        else:
            speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
            time.sleep(7200)

if __name__ == "_main_":
    main()