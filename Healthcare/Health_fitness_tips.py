import pyttsx3
import speech_recognition as sr
import random
import datetime

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


def remind_exercise():
    speak("It's time to do some exercise. Remember to take care of your health!")

def provide_fitness_tips(health_condition):
    if health_condition == "normal":
        tips = ["Remember to stay hydrated throughout the day.", "Include a variety of fruits and vegetables in your diet.",
                "Try to get at least 30 minutes of exercise every day.", "Make sure to get enough sleep for optimal health."]
    elif health_condition == "diabetic":
        tips = ["Monitor your blood sugar levels regularly.", "Follow a balanced diet with controlled carbohydrate intake.",
                "Engage in regular physical activity to help manage your blood sugar levels.",
                "Consult with your healthcare provider for personalized advice."]
    elif health_condition == "hypertensive":
        tips = ["Limit your sodium intake to help control your blood pressure.", "Engage in regular aerobic exercise such as walking, swimming, or cycling.",
                "Monitor your blood pressure regularly and take medications as prescribed by your doctor.",
                "Practice stress-reduction techniques such as deep breathing or meditation."]
    else:
        tips = ["Consult with a healthcare professional for personalized health advice.", "Stay informed about your health condition and follow recommended guidelines.",
                "Make healthy lifestyle choices such as eating a balanced diet and staying physically active.",
                "Listen to your body and seek medical attention if you experience any concerning symptoms."]

    tip = random.choice(tips)
    speak("Here's a fitness tip for you: " + tip)

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "exercise" in query:
            remind_exercise()
        elif "fitness tips" in query:
            speak("What is your current health condition?")
            health_condition = takeCommand().lower()
            provide_fitness_tips(health_condition)
        elif "health and wellness tips" in query:
            speak("Sure! What specific topic are you interested in?")
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